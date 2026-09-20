import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from supabase import create_client
import os
 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
 
# ---------- Setup (runs once, cached) ----------
 
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
 
# A fixed session id keeps this simple: one ongoing conversation for this app.
# (If you ever want separate conversations, you'd generate a unique id per
# session, e.g. with Python's uuid module, and store it in the URL or a login.)
SESSION_ID = "default_session"
 
 
@st.cache_resource
def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    vector_store = Chroma(
        collection_name="crime_and_punishment_bge",
        embedding_function=embedding_model,
        persist_directory="./chroma_db",
    )
    return vector_store
 
 
@st.cache_resource
def load_llm():
    return genai.GenerativeModel(model_name="models/gemini-3.6-flash")
 
 
@st.cache_resource
def load_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)
 
 
vector_store = load_vector_store()
model = load_llm()
supabase = load_supabase()
 
# ---------- Persistence (Supabase) ----------
 
 
def load_history_from_db(session_id: str) -> list[dict]:
    """Fetch all past messages for this session, oldest first."""
    response = (
        supabase.table("chat")
        .select("role, message")
        .eq("session_id", session_id)
        .order("created_at", desc=False)
        .execute()
    )
    # Rename "message" -> "content" to match the shape the rest of the app uses
    return [{"role": row["role"], "content": row["message"]} for row in response.data]
 
 
def save_message_to_db(session_id: str, role: str, message: str) -> None:
    """Persist a single message so it survives an app/session restart."""
    supabase.table("chat").insert(
        {"session_id": session_id, "role": role, "message": message}
    ).execute()
 
 
# ---------- RAG logic ----------
 
 
def format_history(history: list[dict]) -> str:
    """Turn saved (role, content) turns into a readable transcript for the prompt."""
    if not history:
        return "(no previous conversation)"
    lines = []
    for turn in history:
        speaker = "User" if turn["role"] == "user" else "Assistant"
        lines.append(f"{speaker}: {turn['content']}")
    return "\n".join(lines)
 
 
def rewrite_as_standalone_question(question: str, history: list[dict]) -> str:
    """Resolve pronouns/references in a follow-up using history, before retrieval."""
    if not history:
        return question  # first turn, nothing to resolve
 
    conversation_so_far = format_history(history)
 
    rewrite_prompt = f"""Given the conversation history and a follow-up question,
rewrite the follow-up as a standalone question that makes sense with no prior
context, by resolving pronouns and vague references (e.g. "she", "that", "him")
using the history. If the follow-up is already standalone, return it unchanged.
Return ONLY the rewritten question, nothing else.
 
Conversation history:
{conversation_so_far}
 
Follow-up question: {question}
 
Standalone question:"""
 
    response = model.generate_content(rewrite_prompt)
    return response.text.strip()
 
 
def answer_question(question: str, history: list[dict]) -> str:
    # Resolve the question against history BEFORE retrieval, so search targets
    # the right subject (e.g. "she" -> "Sonia") instead of the literal words.
    standalone_question = rewrite_as_standalone_question(question, history)
 
    # Retrieve top relevant chunks using the resolved question
    results = vector_store.similarity_search(standalone_question, k=5)
    context = "\n\n".join(doc.page_content for doc in results)
 
    conversation_so_far = format_history(history)
 
    prompt = f"""You are answering questions about the novel "Crime and Punishment".
Use the retrieved context below to answer the question. You may synthesize and
reasonably interpret across the retrieved passages to form a complete answer,
as long as your answer is grounded in what the context describes. Only say you
don't have enough information if the context is truly unrelated to the question.
 
You are in an ongoing conversation with the user. Use the conversation history
to understand follow-up questions, references to earlier answers (e.g. "he",
"that", "what about her"), and to avoid repeating yourself unnecessarily.
 
Conversation so far:
{conversation_so_far}
 
Retrieved context:
{context}
 
New question: {question}
 
Answer:"""
 
    response = model.generate_content(prompt)
    return response.text
 
 
# ---------- Streamlit UI ----------
 
st.set_page_config(page_title="Crime and Punishment RAG", page_icon="📖")
st.title("📖 Ask Crime and Punishment")
st.caption("Multi-turn RAG chat — history is saved to Supabase and survives a restart.")
 
# Load history from Supabase once per session (instead of starting empty)
if "history" not in st.session_state:
    st.session_state.history = load_history_from_db(SESSION_ID)
 
# Re-display the full conversation so far on every rerun
for turn in st.session_state.history:
    with st.chat_message(turn["role"]):
        st.write(turn["content"])
 
question = st.chat_input("Ask something about the novel...")
 
if question:
    # Show, save (in-memory), and persist (Supabase) the user's message
    with st.chat_message("user"):
        st.write(question)
    st.session_state.history.append({"role": "user", "content": question})
    save_message_to_db(SESSION_ID, "user", question)
 
    # Generate and show the assistant's reply, using history for context
    with st.chat_message("assistant"):
        with st.spinner("Searching the book..."):
            answer = answer_question(question, st.session_state.history)
        st.write(answer)
    st.session_state.history.append({"role": "assistant", "content": answer})
    save_message_to_db(SESSION_ID, "assistant", answer)


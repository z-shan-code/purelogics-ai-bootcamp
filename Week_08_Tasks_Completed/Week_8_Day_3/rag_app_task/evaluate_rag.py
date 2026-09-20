from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import google.generativeai as genai

from dotenv import load_dotenv
import os
import json

from ragas import EvaluationDataset, SingleTurnSample, evaluate
from ragas.llms import llm_factory
from ragas.embeddings.base import embedding_factory

import pandas as pd


from ragas.metrics.collections import(
    Faithfulness,
    ContextPrecision,
    ContextRecall,
    AnswerRelevancy
)


# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)


# --------------------------------------------------
# 2. Questions
# --------------------------------------------------

questions = [
    "Who is Raskolnikov?",
    "Why did Raskolnikov commit the crime?",
    "Who were the victims of the crime?",
    "What punishment did Raskolnikov receive?",
    "Who is Sonia?"
]


# --------------------------------------------------
# 3. Reference answers
# --------------------------------------------------

references = [
    "Raskolnikov is the main protagonist of Crime and Punishment, a former student living in poverty in St. Petersburg.",

    "Raskolnikov committed the murders because he wanted to test his theory that extraordinary people could transgress moral laws, and he was also motivated by poverty and his circumstances.",

    "Raskolnikov killed Alyona Ivanovna, an old pawnbroker, and Lizaveta Ivanovna, her sister, who unexpectedly arrived at the scene.",

    "Raskolnikov was sentenced to eight years of penal servitude in Siberia after confessing to the murders.",

    "Sonia Marmeladova is a young woman who becomes closely connected to Raskolnikov and provides him with compassion and moral support."
]


# --------------------------------------------------
# 4. Load embedding model
# --------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# 5. Load existing Chroma vector store
# --------------------------------------------------

vector_store = Chroma(
    collection_name="crime_and_punishment_bge",
    embedding_function=embedding_model,
    persist_directory="./chroma_db",
)


# --------------------------------------------------
# 6. Gemini model
# --------------------------------------------------

model = genai.GenerativeModel(
    model_name="models/gemini-3.6-flash"
)


# --------------------------------------------------
# 7. Generate answer
# --------------------------------------------------

def generate_answer(question, context):

    prompt = f"""
You are answering questions about the novel
"Crime and Punishment".

Use ONLY the retrieved context below to answer
the question.

Retrieved context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text


# --------------------------------------------------
# 8. Generate/load cached RAG data
# --------------------------------------------------

CACHE_FILE = "rag_evaluation_data.json"


if os.path.exists(CACHE_FILE):

    print("\nLoading previously generated RAG results...")

    with open(CACHE_FILE, "r", encoding="utf-8") as file:
        cached_data = json.load(file)

else:

    print("\nGenerating RAG answers...")

    cached_data = []

    for question, reference in zip(questions, references):

        print("\n" + "=" * 80)
        print("QUESTION:", question)

        # Retrieve documents
        results = vector_store.similarity_search(
            question,
            k=5
        )

        # Extract contexts
        contexts = [
            doc.page_content
            for doc in results
        ]

        # Combine contexts
        context_text = "\n\n".join(contexts)

        # Generate answer
        answer = generate_answer(
            question,
            context_text
        )

        print("\nANSWER:", answer)

        cached_data.append({
            "question": question,
            "contexts": contexts,
            "answer": answer,
            "reference": reference
        })

    # Save generated data
    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            cached_data,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("\nRAG data saved to:", CACHE_FILE)


# --------------------------------------------------
# 9. Build Ragas dataset
# --------------------------------------------------

samples = []

for item in cached_data:

    sample = SingleTurnSample(
        user_input=item["question"],
        retrieved_contexts=item["contexts"],
        response=item["answer"],
        reference=item["reference"]
    )

    samples.append(sample)


evaluation_dataset = EvaluationDataset(
    samples=samples
)


# --------------------------------------------------
# 10. Ragas evaluator LLM
# --------------------------------------------------

client = genai.GenerativeModel(
    "gemini-3.6-flash"
)

evaluator_llm = llm_factory(
    "gemini-3.6-flash",
    provider="google",
    client=client
)

ragas_embeddings = embedding_factory(
    "google"
)

# --------------------------------------------------
# 11. Evaluation metrics
# --------------------------------------------------

metrics = [
    Faithfulness(
        llm=evaluator_llm
    ),

    AnswerRelevancy(
        llm=evaluator_llm,
        embeddings=ragas_embeddings
    ),

    ContextPrecision(
        llm=evaluator_llm
    ),

    ContextRecall(
        llm=evaluator_llm
    )
]


# --------------------------------------------------
# 12. Run Ragas evaluation
# --------------------------------------------------

print("\nStarting Ragas evaluation...")

# results = evaluate(
#     dataset=evaluation_dataset,
#     metrics=metrics
# )


# --------------------------------------------------
# 13. Structured results
# --------------------------------------------------

# results_df = results.to_pandas()

# print("\n")
# print("=" * 80)
# print("RAGAS EVALUATION RESULTS")
# print("=" * 80)

# print(results_df.to_string(index=False))


# # --------------------------------------------------
# # 14. Save results
# # --------------------------------------------------

# results_df.to_csv(
#     "ragas_results.csv",
#     index=False
# )

# print("\nResults saved to: ragas_results.csv")




# ===================================================
rows = []

for item in cached_data:
    row = {
        "question": item["question"],
        "answer": item["answer"],
        "reference": item["reference"],
    }

    row["faithfulness"] = metrics[0].score(
        user_input=item["question"],
        response=item["answer"],
        retrieved_contexts=item["contexts"]
    ).value

    row["answer_relevancy"] = metrics[1].score(
        user_input=item["question"],
        response=item["answer"]
    ).value

    row["context_precision"] = metrics[2].score(
        user_input=item["question"],
        reference=item["reference"],
        retrieved_contexts=item["contexts"]
    ).value

    row["context_recall"] = metrics[3].score(
        user_input=item["question"],
        reference=item["reference"],
        retrieved_contexts=item["contexts"]
    ).value

    rows.append(row)

results_df = pd.DataFrame(rows)

print("\nRAGAS RESULTS:")
print(results_df.to_string(index=False))

results_df.to_csv("ragas_results.csv", index=False)

print("\nResults saved to ragas_results.csv")
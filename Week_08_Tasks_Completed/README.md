# 🔗 Week 8 — Prompt Engineering, LangChain & Retrieval-Augmented Generation (RAG)

> Week 8 marked the shift into Generative AI application development — moving from understanding how LLMs work internally to actually building with them. This week covered how to communicate effectively with LLMs through prompting, and how to ground their responses in real, external data using RAG.

---

## 🧠 What This Week Covered

### ✍️ Prompt Engineering
- Practiced core prompt engineering techniques for getting reliable, structured output from LLMs, including:
  - Iterative prompt refinement
  - Summarizing, inferring, expanding, and transforming text through prompting
  - Building a simple conversational chatbot using prompt design
- Learned how the way a prompt is structured directly affects the quality, accuracy, and consistency of an LLM's response

### 🦜 LangChain
- Introduced to **LangChain**, the most widely used framework for building LLM-powered applications
- Learned how to load and work with external documents (including a full novel — *Crime and Punishment*) as input for downstream LLM tasks

### 🧠 Vector Stores & ChromaDB
- Learned how raw text gets converted into embeddings and stored in a **vector store** for semantic search
- Used **ChromaDB** as the vector database to store and query embedded document chunks

### 📚 Retrieval-Augmented Generation (RAG)
- Built a working **RAG application** — combining document retrieval with LLM generation so responses are grounded in actual source material rather than relying purely on the model's internal knowledge
- Used *Crime and Punishment* (the full novel) as the knowledge base: loaded the text, chunked and embedded it, stored it in ChromaDB, and queried it through a retrieval pipeline
- Practiced evaluating RAG output — checking whether retrieved context actually improved the relevance and accuracy of generated answers

---

## 🧠 Key Takeaways
- Practical skill in prompt engineering — a foundational skill for working with any LLM, regardless of framework
- Hands-on experience with LangChain, the industry-standard framework for LLM application development
- Understanding of the full RAG pipeline: document loading → chunking → embedding → vector storage → retrieval → generation
- First real experience building an AI application that combines an LLM with an external, custom knowledge source — the core pattern behind most production LLM apps today

---

## 🛠️ Tech Stack
`Python` · `LangChain` · `ChromaDB` · `OpenAI / LLM APIs` · `Jupyter Notebook`

## 📁 Folder Structure
```
Week_08_Tasks_Completed/
├── Week_8_Day_1/     → Prompt engineering practice
├── Week_8_Day_2/     → LangChain, document loading, vector stores
├── Week_8_Day_3/     → RAG application — Crime and Punishment (ChromaDB)
└── Week_8_Day_4/     → Continued practice
```

> **Note:** API keys and local vector database files are excluded from this repository via `.gitignore` for security — only source code and notebooks are included.
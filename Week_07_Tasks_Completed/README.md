# ⚡ Week 7 — Transformers: From "Attention Is All You Need" to Hugging Face

> Week 7 was one of the most foundational weeks of the entire bootcamp — this is the architecture behind virtually every modern LLM. Rather than just using pre-built transformer models, the week was spent understanding the architecture from first principles, starting with the paper that started it all.

---

## 🧠 What This Week Covered

### 📄 Studying "Attention Is All You Need"
- Read and studied the original Transformer paper — the foundational research that introduced the self-attention mechanism and replaced recurrence-based architectures (RNNs/LSTMs) in sequence modeling
- Understood *why* this paper was a turning point for the entire field of NLP and, eventually, generative AI as a whole

### 🏗️ End-to-End Transformer Architecture
Covered the full architecture from the ground up, not just at a conceptual level:

- **Historical context** — how sequence modeling evolved from RNNs/LSTMs to attention-based architectures, and what limitations Transformers were built to solve
- **Positional Encoding** — how Transformers, which have no inherent sense of sequence order, are given positional information about tokens
- **Self-Attention & Multi-Head Attention** — the core mechanism that lets the model weigh the relevance of different tokens to one another
- **Encoder-Decoder Architecture** — how the two halves of the original Transformer work together for sequence-to-sequence tasks
- **Advanced techniques** building on the base architecture, used in modern, real-world transformer-based systems

### 🤗 Hugging Face
- Applied transformer concepts practically using the **Hugging Face** ecosystem — working with pre-trained transformer models and tooling used throughout the industry

---

## 🧠 Key Takeaways
- Deep, first-principles understanding of the Transformer architecture — not just how to call a pre-trained model, but how and why it works internally
- Solid grasp of self-attention, positional encoding, and encoder-decoder design
- Practical experience applying these concepts using Hugging Face, bridging theory into real, usable tools
- This week laid the direct foundation for the LLM, RAG, and agentic AI work covered later in the bootcamp

---

## 🛠️ Tech Stack
`Python` · `PyTorch` / `TensorFlow` · `Hugging Face` · `Jupyter Notebook`

## 📁 Folder Structure
```
Week_07_Tasks_Completed/
├── Week_7_Day_1_Task (10 Aug)/     → "Attention Is All You Need" paper study
├── Week_7_Day_2_Task (11 Aug)/     → End-to-end Transformer architecture
├── Week_7_Day_3_Task (12-Aug)/     → Hugging Face — practical application
└── Week_7_Day_4_Task/               → Hugging Face — continued practice
```
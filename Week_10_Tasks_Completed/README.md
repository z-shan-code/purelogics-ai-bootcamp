# 🕸️ Week 10 — LangGraph, Tool Calling & Agentic Workflows

> Week 10 pushed further into agentic AI — moving beyond simple LLM calls into systems that can reason, call external tools, and follow structured, stateful workflows. This is the foundation for building AI that doesn't just respond, but actually *does* things.

---

## 🧠 What This Week Covered

### 🔗 LangChain (Continued) & LangGraph
- Built on Week 8's LangChain foundation and introduced **LangGraph** — a framework for building stateful, multi-step LLM workflows as graphs rather than simple linear chains
- Learned how LangGraph enables more complex agent behavior — branching logic, state management, and multi-step reasoning that a basic chain can't handle

### 🛠️ Tool Calling & Function Calling
- Implemented **tool calling / function calling**, allowing an LLM to decide when to invoke external functions or APIs rather than only generating text
- Understood how this is the core mechanism that turns an LLM from a "text generator" into an "agent" capable of taking real actions
- Practiced defining tools/functions in a way the model can correctly understand and invoke

### 🔑 Working with API Keys
- Handled real API key integration for connecting LLM applications to external services securely
- Practiced managing credentials properly during development (kept out of version control, as reflected in this repo's `.gitignore`)

### 🧯 Error Handling
- Implemented proper error handling around tool calls and API interactions — an essential, often-overlooked skill for building agentic systems that don't silently fail or crash for the wrong reasons
- Learned to build more robust, production-minded AI workflows rather than only "happy path" demos

---

## 🧠 Key Takeaways
- Practical understanding of LangGraph and how it differs from basic LangChain chains
- Hands-on experience implementing tool/function calling — the mechanism behind modern AI agents
- Real-world experience managing API keys securely during development
- Stronger, more production-aware coding practices through deliberate error handling

---

## 🛠️ Tech Stack
`Python` · `LangChain` · `LangGraph` · `LLM APIs` · `Jupyter Notebook`

## 📁 Folder Structure
```
Week_10_Tasks_Completed/
├── week_10_lab_1/     → LangGraph fundamentals
├── week_10_lab_2/     → Tool calling / function calling
└── week_10_lab_3/     → API integration & error handling
```

> **Note:** API keys are excluded from this repository via `.gitignore` for security — only source code and notebooks are included.
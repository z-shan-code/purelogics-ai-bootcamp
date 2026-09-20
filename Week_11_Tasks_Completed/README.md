# 🔌 Week 11 — Model Context Protocol (MCP): Building a Task Manager MCP Server

> Week 11 closed out the bootcamp by going straight to the frontier of agentic AI tooling — the **Model Context Protocol (MCP)**, the emerging standard for how AI assistants connect to external tools and data. Rather than just learning the theory, this week meant designing, building, testing, and presenting a fully working MCP server from scratch.

---

## 🧠 What Is MCP?

The Model Context Protocol is a standardized way for an AI assistant to talk to external programs and data sources — instead of every AI tool needing its own custom, one-off connector for every application, MCP provides a common protocol both sides can speak. This week was spent understanding and building both halves of that conversation:

- **MCP Server** — a program exposing a menu of actions ("tools") an AI assistant can call
- **MCP Client** — the program on the other side (the AI assistant, or a testing tool) that reads that menu and invokes tools on it
- **Tools** — individual actions a server exposes, each with a name, description, and input schema
- **Resources** — optional, read-only data a server can expose (distinct from tools, which perform actions)
- **Transport** — the channel client and server communicate over (this project used `stdio`, the simplest local transport)

---

## 🛠️ Project Built: Task / To-Do Manager MCP Server

Designed and implemented a complete MCP server exposing task-management functionality to an AI assistant, including:

| Tool | Function |
|---|---|
| `add_task` | Create a new task |
| `list_tasks` | Retrieve all tasks |
| `get_task` | Retrieve a single task by ID |
| `complete_task` | Mark a task as completed |
| `delete_task` | Remove a task |

**Bonus resource:** `tasks://pending` — a read-only view exposing all pending (incomplete) tasks directly to the connected AI assistant.

---

## 🧩 How the Week Was Structured

### Day 1 — Understanding MCP Before Building
- Installed the MCP Python SDK and ran a pre-built sample MCP server to see the protocol working end-to-end before writing any original code
- Used **MCP Inspector** to connect to the sample server and call its tools directly, observing how input and output actually flow through the protocol
- Studied the sample server's source code to understand how a tool is named, how its input schema is defined, and where its actual logic runs
- Planned the Task Manager project: defined all 5 tools with clear names and plain-English descriptions before writing a single line of implementation code

### Day 2 — Building the Server (Part 1)
- Set up the project structure (`server.py`, `README.md`, `requirements.txt`) and initialized the MCP server object
- Implemented the first 2–3 tools one at a time, testing each fully in MCP Inspector before moving to the next — rather than writing all tools at once and debugging everything together
- Used simple in-memory storage to keep the implementation focused on the protocol itself rather than infrastructure

### Day 3 — Building the Server (Part 2) & Hardening
- Completed the remaining tools to reach the full 5-tool set
- Added proper **error handling** — every tool now returns a clear, descriptive error instead of crashing when given missing or invalid input
- Implemented the bonus `tasks://pending` resource
- Wrote complete project documentation, including setup instructions and one example call per tool
- Ran full end-to-end scenarios (e.g. "add a task, then list all pending tasks") to confirm the server behaves correctly as a real user would use it

### Day 4 — Live Demo & Viva
- Presented the working server live, demonstrating real tool calls through MCP Inspector
- Walked through the design decisions behind each tool and how task data was stored
- Answered conceptual questions on MCP fundamentals — the client/server relationship, tools vs. resources, transport, and schema validation — reinforcing not just *that* the server worked, but *why* it was built the way it was

---

## 🧠 Key Takeaways
- Practical understanding of MCP as a protocol — not just using a pre-built MCP integration, but building the server side from the ground up
- Hands-on experience designing clear, well-scoped tool schemas that an AI assistant can reliably call
- Real experience testing an MCP server directly with MCP Inspector before ever connecting it to an actual AI assistant
- Reinforced good engineering habits: incremental building and testing (one tool at a time), graceful error handling, and clear documentation
- This week directly connects to the agentic AI concepts from LangGraph and tool/function calling in Week 10 — MCP is a standardized way of solving the same underlying problem: giving an AI system safe, well-defined access to real-world actions

---

## 🛠️ Tech Stack
`Python` · `MCP Python SDK` · `MCP Inspector` · `stdio Transport`

## 📁 Folder Structure
```
Week_11_Tasks_Completed/
├── Day_1_MCP_Fundamentals/         → Exploring a pre-built sample MCP server
├── Day_2_Build_Part_1/             → Initial tool implementation
├── Day_3_Build_Part_2/             → Remaining tools, error handling, documentation
├── Day_4_Demo_and_Viva/            → Final presentation materials
└── task_manager_mcp_server/        → Final, complete MCP server project
```

> **Note:** Update the folder names above to match your actual local structure before committing.
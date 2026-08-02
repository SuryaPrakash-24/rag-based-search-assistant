# RAG-based Search Assistant (Claude + Python)

A lightweight AI agent built using langchain and the Anthropic Claude API. The agent reads the document(s) (PDF files), breaks them down into smaller chunks, stores them in a local vector store and retreive results based on the user's query.

The project includes one tool:

- **Document Search** — fetches the relevant results from the document(s).

---

## Raw Python vs LangChain

The previous version implemented the agent loop manually, which made the mechanics of tool calling, error handling, and message passing explicit. The LangChain version is more concise and handles much of that orchestration for me. I would choose raw Python when I need maximum control or want to understand/debug the underlying flow, and LangChain when I want to build a more complete application without maintaining that orchestration myself.

---

## What is RAG?

Instead of asking Claude to answer a question using only what it already knows, this project gives it relevant information from a document first. The document is split into smaller pieces and stored in a vector store. When a user asks a question, the system searches those pieces for information related to the question and gives the relevant content to Claude. Claude can then use that retrieved context to generate the answer.

---

## How it works

```

                  ┌─────────────────┐
                  │      PDF        │
                  └────────┬────────┘
                           ↓
                    Load + Split
                           ↓
                    Chroma Store
                           │
                           │
User Question              │
      │                    │
      ▼                    │
    Claude                 │
      │                    │
      │ decides            │
      ▼                    │
 search_resume() ──────────┘
      │
      ▼
Relevant document chunks
      │
      ▼
    Claude
      │
      ▼
 Final answer
```

---

## Tech stack

| Layer         | Technology                          |
| ------------- | ----------------------------------- |
| LLM           | Claude Haiku 4.5                    |
| Language      | Python                              |
| Framework     | LangChain                           |
| Document type | PDF                                 |
| Vector store  | ChromaDB                            |
| Embeddings    | `all-MiniLM-L6-v2` (Chroma default) |
| Agent         | LangChain Agent                     |

---

## Project structure

```text
rag-based-search-assistant/
│
├── data/            # PDFs used by the application
│   └── .gitkeep
│
├── agent.py         # Claude + LangChain agent and document-search tool
├── rag.py           # PDF loading, chunking, embeddings, vector store, retrieval
├── main.py          # CLI / user interaction
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting started

### Prerequisites

- Python 3.10+

### 1. Clone the repository

```bash
git clone https://github.com/[username]/rag-based-search-assistant.git
cd rag-based-search-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Claude API key

Sign up on [platform.claude.com](https://platform.claude.com/), if not done already, and generate a new API key.

**Linux / macOS**

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

**Windows (PowerShell)**

```powershell
setx ANTHROPIC_API_KEY "your_api_key_here"
```

Restart the terminal after setting the variable.

### 4. Place your document

Copy the target PDF into the data/ folder before running the code.

### 5. Run the code

```bash
python main.py
```

The Chunking and vector store setup takes ~40-50 secs and the Claude API connection takes ~10–15 seconds. It keeps running until the user provides 'exit' or 'quit' as the input.

## Example

```text
Ask something: What is the main objective of the project?

The main objective is ...
```

Type `exit` or `quit` to stop the program.

---

## Pipeline Architecture

```
PDF
 │
 ▼
Load document
 │
 ▼
Split into chunks
 │
 ▼
Create embeddings
 │
 ▼
Store in vector store
 │
 │
 │       User question
 │             │
 │             ▼
 │       Search vector store
 │             │
 │             ▼
 │      Relevant chunks
 │             │
 └─────────────┤
               ▼
            Claude
               │
               ▼
         Final answer

```

## License

MIT

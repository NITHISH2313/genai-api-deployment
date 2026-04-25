# Mallareddy College AI Chatbot

A RAG (Retrieval-Augmented Generation) powered AI chatbot for Mallareddy Engineering College, built with FastAPI, LangChain, ChromaDB, and Groq's LLaMA model. Ask anything about admissions, fees, placements, exams, and more.

---

## Features

- RAG Pipeline — Retrieves relevant college information before answering
- Groq LLaMA 3.1 — Ultra-fast inference with `llama-3.1-8b-instant`
- HuggingFace Embeddings — Uses `all-MiniLM-L6-v2` for semantic search
- ChromaDB Vector Store — Persistent local vector database
- FastAPI Backend — Clean REST API with auto-generated Swagger docs
- CORS Enabled — Ready to connect with any frontend

---

## Tech Stack

| Layer         | Technology                      |
|---------------|---------------------------------|
| API Framework | FastAPI                         |
| LLM           | Groq — LLaMA 3.1 8B Instant    |
| Embeddings    | HuggingFace — all-MiniLM-L6-v2 |
| Vector Store  | ChromaDB                        |
| Orchestration | LangChain                       |
| Server        | Uvicorn                         |

---

## Project Structure
mallareddy-college-ai/
│
├── api.py              # Main FastAPI application
├── college_db/         # ChromaDB persistent vector store (auto-created)
├── requirements.txt    # Python dependencies
└── README.md

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mallareddy-college-ai.git
cd mallareddy-college-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Groq API Key

Open `api.py` and replace the placeholder with your actual Groq API key:

```python
api_key = "your_groq_api_key_here"
```

Get your free API key at https://console.groq.com

### 5. Run the Server

```bash
python api.py
```

The server starts at: `http://localhost:8000`

---

## Requirements

Create a `requirements.txt` with the following:
fastapi
uvicorn
pydantic
langchain
langchain-groq
langchain-huggingface
langchain-chroma
langchain-text-splitters
langchain-core
chromadb
sentence-transformers

---

## API Endpoints

| Method | Endpoint  | Description                          |
|--------|-----------|--------------------------------------|
| GET    | /         | Welcome message and available routes |
| GET    | /health   | Check server status                  |
| GET    | /info     | College static information           |
| POST   | /ask      | Ask a question to the AI chatbot     |
| GET    | /docs     | Auto-generated Swagger UI            |

---

## Usage Example

### Ask a Question

Request:

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the fee for BTech CSE?"}'
```

Response:

```json
{
  "question": "What is the fee for BTech CSE?",
  "answer": "The BTech CSE fee is 85,000 per year. Scholarships are also available.",
  "status": "success"
}
```

### Check Health

```bash
curl http://localhost:8000/health
```

Response:

```json
{
  "status": "healthy",
  "model": "llama-3.1-8b-instant"
}
```

---

## How RAG Works
User Question
|
v
HuggingFace Embeddings  -->  ChromaDB Vector Search
|
v
Top 3 Relevant Chunks
|
v
Groq LLaMA 3.1 (with context)
|
v
Final Answer

1. The user's question is converted into a vector using HuggingFace embeddings
2. ChromaDB retrieves the top 3 most semantically similar document chunks
3. The retrieved chunks and the question are passed to LLaMA 3.1 via Groq
4. The model generates an answer based only on the retrieved context

---

## Knowledge Base

The chatbot currently covers the following topics:

- College Overview — Location, programs, affiliation, and student count
- Exam Rules — Attendance policy, internal and external exams, results timeline
- Fee Structure — Branch-wise fees, hostel charges, and available scholarships
- Placements — Salary packages, top recruiting companies, and placement rate

To extend the knowledge base, add more strings to the `documents` list in `api.py` and restart the server.

---

## Interactive API Docs

Once the server is running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Author

Built for Mallareddy Engineering College, Hyderabad.


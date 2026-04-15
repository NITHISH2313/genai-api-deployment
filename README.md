Mallareddy College AI
RAG-Based Question Answering System
Overview
Mallareddy College AI is a production-oriented Retrieval-Augmented Generation (RAG) application designed to provide accurate, context-aware responses to college-related queries.
The system integrates Large Language Models (LLMs) with a custom knowledge base using vector search to ensure reliable and grounded answers.
It is built using modern AI frameworks such as LangChain, Groq, HuggingFace, and ChromaDB, and deployed through a scalable FastAPI backend.
Key Features
Retrieval-Augmented Generation (RAG) pipeline
Context-aware AI responses using custom documents
FastAPI-based RESTful API architecture
Vector similarity search with ChromaDB
HuggingFace-based embedding generation
LLM inference using Groq (Llama 3.1)
Modular and production-ready backend design
Technology Stack
Backend: FastAPI, Uvicorn
LLM: Groq (Llama 3.1 – 8B Instant)
Framework: LangChain
Embeddings: HuggingFace Transformers
Vector Database: ChromaDB
Programming Language: Python
System Architecture
Documents are ingested and split into smaller chunks
Each chunk is converted into vector embeddings
Embeddings are stored in a Chroma vector database
User query is converted into embedding
Relevant document chunks are retrieved
LLM generates a response using retrieved context
Project Structure
├── main.py  
├── college_db/  
├── requirements.txt  
└── README.md  
Setup and Installation
Clone Repository
git clone https://github.com/NITHISH2313/mallareddy-college-ai.git  
cd mallareddy-college-ai  
Create Virtual Environment
python -m venv venv  
Activate environment:
Windows:
venv\Scripts\activate  
Mac/Linux:
source venv/bin/activate  
Install Dependencies
pip install -r requirements.txt  
Environment Configuration
Create a .env file in the root directory:
GROQ_API_KEY=your_api_key_here  
Load environment variables in your application:
from dotenv import load_dotenv  
import os  

load_dotenv()  
api_key = os.getenv("GROQ_API_KEY")  
Add .env to .gitignore:
.env  
Sensitive credentials are managed securely using environment variables and are excluded from version control.
Running the Application
python main.py  
The server will start at:
http://localhost:8000  
API Endpoints
Base Endpoint
GET /
Returns service status and available routes
Health Check
GET /health
Returns API and model status
Ask Question (RAG)
POST /ask
Request Body:
{
  "question": "What is the fee for CSE?"
}
Response:
{
  "question": "What is the fee for CSE?",
  "answer": "85000 per year.",
  "status": "success"
}
College Information
GET /info
API Documentation
Swagger UI:
http://localhost:8000/docs  
Use Cases
AI-powered college helpdesk systems
Domain-specific chatbot applications
Educational query automation
Knowledge-based AI assistants
Future Enhancements
Integration with real-world datasets (PDFs, databases)
Frontend development (React / Next.js)
Authentication and user management
Cloud deployment (AWS / GCP / Azure)
Advanced retrieval techniques (hybrid search, re-ranking)
Author
Nithish K
Generative AI Developer
GitHub: https://github.com/NITHISH2313
Email: nithishkairamkonda27@gmail.com
License
This project is intended for educational and demonstration purposes.

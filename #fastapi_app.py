#fastapi_app
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
import uvicorn

# ===== SETUP =====
app = FastAPI(
    title="Mallareddy College AI",
    description="RAG based AI chatbot for college queries",
    version="1.0.0"
)

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ===== DOCUMENTS =====
documents = [
    """Mallareddy Engineering College is located in Hyderabad.
    BTech programs in CSE, ECE, EEE, Mechanical and Civil.
    Established in 2001, affiliated to JNTUH.
    Total students: 5000.""",

    """Exam Rules:
    75% attendance required for exams.
    Internal exams every month.
    External exams at end of semester.
    Results announced within 30 days.""",

    """Fee Structure:
    BTech CSE: 85000 per year.
    BTech ECE: 80000 per year.
    Hostel: 60000 per year.
    Scholarships available.""",

    """Placements:
    Average package: 4.5 LPA.
    Highest package: 18 LPA.
    Top companies: TCS, Infosys, Wipro, Cognizant.
    Placement rate: 75%."""
]

# ===== BUILD RAG =====
print("building RAG system...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
chunks = splitter.create_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./college_db"
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

api_key = "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"  # paste your key!
llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)

template = """You are a helpful assistant for
Mallareddy Engineering College.
Answer based on context only.
If unsure say "I don't know".

Context: {context}
Question: {question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)

def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs,
     "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("RAG system ready! ✅")

# ===== REQUEST MODEL =====
class Question(BaseModel):
    question: str

class Answer(BaseModel):
    question: str
    answer: str
    status: str

# ===== API ENDPOINTS =====
@app.get("/")
def home():
    return {
        "message": "Welcome to Mallareddy College AI!",
        "status": "running",
        "endpoints": ["/ask", "/health", "/docs"]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "model": "llama-3.1-8b-instant"}

@app.post("/ask", response_model=Answer)
def ask_question(body: Question):
    try:
        if not body.question:
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty!"
            )

        answer = rag_chain.invoke(body.question)

        return Answer(
            question=body.question,
            answer=answer,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/info")
def college_info():
    return {
        "college": "Mallareddy Engineering College",
        "location": "Hyderabad",
        "programs": ["CSE", "ECE", "EEE", "Mechanical", "Civil"],
        "established": 2001,
        "students": 5000
    }

# ===== RUN SERVER =====
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
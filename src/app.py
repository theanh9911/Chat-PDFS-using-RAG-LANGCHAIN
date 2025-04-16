import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from src.base.llm_model import get_hf_llm
from src.rag.main import build_rag_chain, InputQA, OutputQA

# Disable tokenizer parallelism to avoid warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load your HuggingFace LLM with custom temperature
llm = get_hf_llm(temperature=0.9)

# Define the path to your document source
genai_docs = "./data_source/generative_ai"

# Build the RAG chain using your documents
genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain’s Runnable interfaces",
)

# Enable CORS for development/testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Health check route
@app.get("/check")
async def check():
    return {"status": "ok"}

# Main RAG inference endpoint
@app.post("/generative_ai", response_model=OutputQA)
async def generative_ai(inputs: InputQA):
    answer = genai_chain.invoke(inputs.question)
    return {"answer": answer}

# LangServe playground for interaction/testing
add_routes(
    app,
    genai_chain,
    playground_type="default",
    path="/generative_ai"
)


#pip install --upgrade accelerate bitsandbytes
#pip install httpx==0.27.0

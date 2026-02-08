import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is not set. Add it to your .env file.")

from core.llm import chat_llm

app = FastAPI(title="ATLAS")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    text = req.message.strip()
    if not text:
        return ChatResponse(reply="Hello?")
    
    try:
        reply = chat_llm(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")
    
    return{"reply":reply}
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is not set")

from core.llm import Chat

app = FastAPI(title="ATLAS")

chat_engine = Chat()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    text = req.message.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Can't send an empty message")

    try:
        reply = chat_engine.chat(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")
    
    chat_engine.conversation.print_conversation()

    return ChatResponse(reply=reply)
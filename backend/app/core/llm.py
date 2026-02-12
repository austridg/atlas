import os
from openai import OpenAI
from pathlib import Path

from core.memory.conversation_history import *

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_PATH = Path(__file__).resolve().parents[1] / "context" / "system_prompt.txt"

def load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")

def chat_llm(message: str) -> str:
    add_user_msg(message)

    system_prompt = load_system_prompt()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *conversation,
        ],
        temperature=0.3
    )

    reply = response.choices[0].message.content

    add_bot_msg(response)

    # debugging
    # print_conversation()

    return reply
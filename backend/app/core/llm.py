import os
from openai import OpenAI
from pathlib import Path

# configured openai connection
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_PATH = Path(__file__).resolve().parents[1] / "private" / "system_prompt.txt"

def load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")

def chat_llm(message: str) -> str:
    system_prompt = load_system_prompt()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
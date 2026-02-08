import os
from openai import OpenAI

# configured openai connection
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_llm(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are Atlas, a helpful personal AI assistant."},
            {"role": "user", "content": message},
        ],
    )

    return response.choices[0].message.content
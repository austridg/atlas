import os
from openai import OpenAI
from pathlib import Path

from core.memory.conversation_history import Conversation


class Chat:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt_path = Path(__file__).resolve().parents[1] / "context" / "test_important_info.txt"
        self.system_prompt = prompt_path.read_text(encoding="utf-8")

        self.conversation = Conversation()

    def chat(self, message: str) -> str:
        self.conversation.add_user_msg(message)

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.conversation.get_messages()
        ]

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.3
        )

        reply = response.choices[0].message.content

        self.conversation.add_assistant_msg(reply)

        return reply

    def reset(self) -> None:
        self.conversation.delete_conversation()
# import db
import json

class Conversation:

    def __init__(self):
        self.messages = []

    def get_messages(self):
        return self.messages
    
    def check_msg_limit(self) -> bool:
        return len(self.messages) >= 5
    
    def add_user_msg(self, message: str) -> None:
        if self.check_msg_limit():
            self.delete_conversation()
        self.messages.append({"role" : "user","content" : message})

    def add_assistant_msg(self, message: str) -> None:
        if self.check_msg_limit():
            self.delete_conversation()
        self.messages.append({"role" : "assistant","content" : message})

    def delete_conversation(self) -> None:
        self.messages.clear()

    def save_conversation(self,filename="conversation.json") -> None:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(self.messages,file,indent=4)

    def print_conversation(self) -> None:
        for msg in self.messages:
            print(f"{msg['role']} : {msg['content']}")
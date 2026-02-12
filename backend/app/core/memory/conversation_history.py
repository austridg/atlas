# import db
import json

conversation = []

def get_conversation():
    return conversation;

def add_user_msg(message: str) -> None:
    if len(conversation) >= 5:
        delete_conversation()
    conversation.append({"role" : "user","content" : message})

def add_bot_msg(message: str) -> None:
    if len(conversation) >= 5:
        delete_conversation()
    conversation.append({"role" : "assistant","content" : message})

def delete_conversation() -> None:
    conversation.clear()

def save_conversation(conversation,filename="conversation.json") -> None:
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(conversation,file,indent=4)

# debugging
def print_conversation() -> None:
    for msg in conversation:
        print(f"{msg['role']} : {msg['content']}")
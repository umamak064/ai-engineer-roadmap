# Build: A ChatMessage Pydantic model for your future chatbot. What it should do: Fields: role (must be
# "user" , "assistant" , or "system" — use Literal ), content: str (1–4000 characters, use
# Field(min_length=1, max_length=4000) ). Test it with valid and invalid data, print both results. Files:
# week1/day02_chat_message.py

from pydantic import BaseModel,Field
from typing import Literal

class ChatMessage(BaseModel):
    role:Literal['user','assistant','system']
    content:str=Field(min_length=1, max_length=4000)
try:
    bad=ChatMessage(role="admin",content="i m user")
    print(bad)
except Exception as e:
    print("ERROR", e)        

msg=ChatMessage(role="user",content="i m user")  
print (msg) 

# CHALLENGE
# Write a function normalize_message(raw: dict) -> ChatMessage . Input is a messy dict like {"Role": "USER",
# "Content": "hi"} (wrong casing on keys and values). Fix the casing, then create a valid ChatMessage from it.
# If it still fails, catch the error and return None instead of crashing. Try for 20–30 minutes before looking
# anything up.

def normalize_message(dict):
    fix_dict={}
    for key,value in dict.items():
        if key.lower()== "role":
           fix_dict[key.lower()]=value.lower()
        else:
            fix_dict[key.lower()]=value



    try:
        return ChatMessage(**fix_dict)
    except Exception as e:
        print("Error:" ,e)
        return None

valid_dict = {"Role": "USER", "Content": "hi"}
print(normalize_message(valid_dict))

invalid_dict = {"Role": "HACKER", "Content": "hi"}
print(normalize_message(invalid_dict))

    
import os
from dotenv import load_dotenv
from groq import Groq
import argparse

load_dotenv()
parser=argparse.ArgumentParser()
parser.add_argument("--system", default="you are a helpful assistant")
args=parser.parse_args()

messages=[
    {
        "role": "system",
        "content": args.system
    }
]

class Chatbot:
    def __init__(self, system_prompt):
        self.client = Groq()
        self.system_prompt = system_prompt
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]

    def send(self, user_text):
        # step 1: user_text ko self.messages me append karo (role="user")
        self.messages.append(
            {
            "role":"user",
            "content":user_text
            }
            )
        
        # step 2: self.client.chat.completions.create(...) call karo, messages=self.messages de kar
        chat_completion=self.client.chat.completions.create(
            messages=self.messages, #puri messages list groq ko jaigi
            model="openai/gpt-oss-120b",
            temperature=0.7,

        )
        # step 3: reply nikalo chat_completion.choices[0].message.content se
        assistant_response= chat_completion.choices[0].message.content
        
        # step 4: reply ko bhi self.messages me append karo (role="assistant")
        self.messages.append(
                    {
                        "role":"assistant",
                        "content":assistant_response
                    }
                ) 
        
        # step 5: reply return karo
        return assistant_response

    def reset(self):
        # self.messages ko wapas sirf system message tak le aao
        self.messages=[
            {
                "role": "system",
                "content": self.system_prompt
                }
            ]
        return self.messages

    def get_history(self):
        # self.messages wapas karo
        return self.messages

bot = Chatbot(args.system)

while True:
    response = input("You: ")
    if response.lower().strip() == "exit":
        break
    reply = bot.send(response)
    print(f"Assistant: {reply}\n")    

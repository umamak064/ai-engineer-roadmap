
from dotenv import load_dotenv
from groq import Groq
import argparse
load_dotenv()
client=Groq()
parser=argparse.ArgumentParser()
parser.add_argument("--system", default="you are a helpful assistant")
args=parser.parse_args()

messages=[
    {
        "role": "system",
        "content": args.system
    }
]
while True:
    response=input("You: ")
    if response.lower().strip()=="exit":
        break
    # Append the user message to the ongoing conversation history
    messages.append(
        {
            "role":"user",
            "content": response
        }
    )

    #Send messages to the AI model       
    chat_completion=client.chat.completions.create(
        messages=messages, #puri messages list groq ko jaigi
        model="openai/gpt-oss-120b",
        temperature=0.7,
    )

    # Extract the assistant's response
    assistant_response= chat_completion.choices[0].message.content
    print(f"Assistant: {assistant_response}\n")

    messages.append(
        {
            "role":"assistant",
            "content":assistant_response
        }
    ) 


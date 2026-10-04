# 1. Send one message with no system prompt — see the default behavior.
# 2. Add a system prompt like “You are a pirate” — see the difference.
# 3. Send the same question 3 times at temperature=0 — notice the answers are nearly identical.
# 4. Send the same question 3 times at temperature=1.5 — notice the answers vary more.
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


client=Groq()
       
chat_completion=client.chat.completions.create(

    messages=[
        {
            "role":"system",
            "content":"you are helpfull assistant"
        },
        {
            "role":"user",
            "content":"hi! tell me what time is it"
        }
    ],
    model="openai/gpt-oss-120b",
    temperature=1.5,

)
print(chat_completion.choices[0].message.content)

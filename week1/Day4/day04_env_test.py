import os
from dotenv import load_dotenv

load_dotenv()

llm_provider=os.getenv("GROQ_API_KEY")
print(llm_provider)
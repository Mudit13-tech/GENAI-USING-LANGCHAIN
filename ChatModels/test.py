from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

print("Key exists:", bool(os.getenv("GROQ_API_KEY")))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "What is the capital of USA?"}
    ]
)

print(response.choices[0].message.content)

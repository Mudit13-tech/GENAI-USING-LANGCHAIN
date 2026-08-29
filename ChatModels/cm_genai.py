from asyncio import streams
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

AiModel = ChatGroq(model="qwen/qwen3.8-27b",temperature=1.5)
result = AiModel.invoke("SUGGEST ME 5 INDIAN DISHES not a large description of food ")
print(result.content)
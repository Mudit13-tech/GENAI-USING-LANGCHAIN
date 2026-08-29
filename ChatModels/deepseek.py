from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv()

AiModel = ChatDeepSeek(model="deepseek-chat")  # or "deepseek-reasoner" for R1
result = AiModel.invoke("SUGGEST ME 5 INDIAN DISHES")
print(result.content)

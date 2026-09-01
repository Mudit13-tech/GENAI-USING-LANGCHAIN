from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

AiModel = ChatHuggingFace(llm=llm)
result = AiModel.invoke("SUGGEST ME 5 INDIAN DISHES")
print(result.content)
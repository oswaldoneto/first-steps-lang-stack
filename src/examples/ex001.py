from langchain.chat_models import init_chat_model
from rich import print 

llm = init_chat_model("openai:gpt-5-mini")

response = llm.invoke('Olá, tudo bem?')

print(response)

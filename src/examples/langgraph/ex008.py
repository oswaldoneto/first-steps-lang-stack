from typing import TypedDict, Annotated, Sequence
from rich import print
from rich.markdown import Markdown

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END, add_messages
from langchain.chat_models import init_chat_model

llm = init_chat_model("openai:gpt-5-mini")

# 1. Defino meu state
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
     
# 2. Defino meu node 
def call_llm(state: AgentState) -> AgentState:
    llm_result = llm.invoke(state["messages"])
    return {'messages':[llm_result]} 

# 3. Crio o StateGraph
builder = StateGraph(
    AgentState, context_schema=None, input_schema=AgentState, output_schema=AgentState
)

# 4. Adicione nodes ao grafo
builder.add_edge(START, "call_llm")
builder.add_node("call_llm", call_llm)
builder.add_edge("call_llm", END)

# 5. Compilar o grafo
checkpointer = InMemorySaver() 
graph = builder.compile(checkpointer=checkpointer)

if __name__ == '__main__':

    # 6. Usar o grafo
    while True:
        user_input = input('Digite sua mensagem: ')
        print(Markdown('---'))
        
        if user_input.lower() in ['q','quit', 'exit']:
            print("Bye")
            print(Markdown('---'))
            break

        human_message = HumanMessage(user_input)
        result = graph.invoke({'messages': [human_message]})
        current_messages = result['messages']

        print(Markdown(str(result['messages'][-1].content)))
        print(Markdown('---'))





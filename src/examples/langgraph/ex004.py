
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph
from rich import print
import operator

# Define o estado do meu grafo
class State(TypedDict):
    nodes_path: Annotated[list[str], operator.add]

# Define nodes
def node_a(state: State):
    nodes_path = state['nodes_path']
    output_state: State =  {'nodes_path': ["A"]}
    print('> node_a', f'{state=}', f'{output_state=}')
    return output_state

def node_b(state: State):
    nodes_path = state['nodes_path']
    output_state: State =  {'nodes_path': ["B"]}
    print('> node_b', f'{state=}', f'{output_state=}')
    return output_state

# Define os nodes do grafo
builder = StateGraph(State)
builder.add_node('A', node_a)
builder.add_node('B', node_b)

# Define as arestas do grafo 
builder.add_edge("__start__","A") 
builder.add_edge("A", "B")
builder.add_edge("B","__end__")

# Compila o grafo
graph = builder.compile()

# Pegar o resultado 
response = graph.invoke({"nodes_path": []})

print(f'{response}')

#print(graph.get_graph().draw_mermaid())
#graph.get_graph().draw_mermaid_png(output_file_path='file.png') 
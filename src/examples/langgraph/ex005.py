
from dataclasses import dataclass

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from rich import print
import operator

# Define o estado do meu grafo
@dataclass
class State:
    nodes_path: Annotated[list[str], operator.add]

# Define nodes
def node_a(state: State):
    output_state: State = State(nodes_path=['A'])
    print('> node_a', f'{state=}', f'{output_state=}')
    return output_state

def node_b(state: State):
    output_state: State = State(nodes_path=['B'])
    print('> node_b', f'{state=}', f'{output_state=}')
    return output_state

# Define os nodes do grafo
builder = StateGraph(State)
builder.add_node('A', node_a)
builder.add_node('B', node_b)

# Define as arestas do grafo 
builder.add_edge(START,"A") 
builder.add_edge("A", "B")
builder.add_edge("B",END)

# Compila o grafo
graph = builder.compile()

# Pegar o resultado 
response = graph.invoke(State(nodes_path=[]))

print(f'{response}')

#print(graph.get_graph().draw_mermaid())
#graph.get_graph().draw_mermaid_png(output_file_path='file.png') 
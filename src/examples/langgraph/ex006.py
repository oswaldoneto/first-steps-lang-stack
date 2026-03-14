
from dataclasses import dataclass
from typing import Annotated, TypedDict, Literal

from langgraph.graph import StateGraph, START, END
from rich import print
import operator

# Define o estado do meu grafo
@dataclass
class State:
    nodes_path: Annotated[list[str], operator.add]
    current_number: int = 0

# Define nodes
def node_a(state: State):
    output_state: State = State(nodes_path=['A'], current_number=state.current_number)
    print('> node_a', f'{state=}', f'{output_state=}')
    return output_state

def node_b(state: State):
    output_state: State = State(nodes_path=['B'], current_number=state.current_number)
    print('> node_b', f'{state=}', f'{output_state=}')
    return output_state

def node_c(state: State):
    output_state: State = State(nodes_path=['C'], current_number=state.current_number)
    print('> node_c', f'{state=}', f'{output_state=}')
    return output_state

# Função condicional 
def the_conditiional(state: State) -> Literal['goes_to_B','goes_to_C']:
    if state.current_number >= 50:
        return "goes_to_b"
    return "goes_to_c"

# Define os nodes do grafo
builder = StateGraph(State)
builder.add_node('A', node_a)
builder.add_node('B', node_b) 
builder.add_node('C', node_c)

# Define as arestas do grafo 
builder.add_edge(START,"A") 
builder.add_conditional_edges('A', the_conditiional, {
    "goes_to_b": "B",
    "goes_to_c": "C"
})
builder.add_edge("B", END)
builder.add_edge("C", END)
 
# Compila o grafo
graph = builder.compile()

# Pegar o resultado 
print()
response = graph.invoke(State(nodes_path=[]))
print(f"{response=}")
print(f'{response}')
print()

print()
response = graph.invoke(State(nodes_path=[], current_number=51))
print(f"{response=}")
print(f'{response}')
print()

#print(graph.get_graph().draw_mermai d())
graph.get_graph().draw_mermaid_png(output_file_path='file.png') 
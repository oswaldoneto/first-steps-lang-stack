# First Steps Lang Stack

Exemplos práticos para aprender LangChain e LangGraph com OpenAI, usando `uv`.

## Requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Configuração

1. Crie o arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY="sua_chave_aqui"
OPENAI_MODEL="gpt-5-mini"
```

2. Instale/sincronize as dependências:

```bash
uv sync
```

## Estrutura dos exemplos

### LangChain

- `src/examples/langchain/ex001.py`: chamada simples ao modelo.
- `src/examples/langchain/ex002.py`: uso de `SystemMessage` + `HumanMessage`.
- `src/examples/langchain/ex003.py`: chat interativo com histórico de mensagens.

### LangGraph

- `src/examples/langgraph/ex004.py`: grafo linear (`START -> A -> B -> END`) com estado em `TypedDict`.
- `src/examples/langgraph/ex005.py`: mesma ideia do `ex004`, usando `dataclass` no estado.
- `src/examples/langgraph/ex006.py`: fluxo condicional, roteando de `A` para `B` ou `C`.
- `src/examples/langgraph/ex007.py`: chat com `StateGraph` e estado de mensagens (`add_messages`).
- `src/examples/langgraph/ex008.py`: variação do `ex007` com `checkpointer` em memória (`InMemorySaver`).

## Como executar

Use sempre a raiz do projeto:

```bash
cd /Users/oswaldo/Projects/dio/first-steps-lang-stack
```

### Executar um exemplo específico

```bash
uv run --env-file=.env python src/examples/langchain/ex001.py
uv run --env-file=.env python src/examples/langchain/ex002.py
uv run --env-file=.env python src/examples/langchain/ex003.py

uv run --env-file=.env python src/examples/langgraph/ex004.py
uv run --env-file=.env python src/examples/langgraph/ex005.py
uv run --env-file=.env python src/examples/langgraph/ex006.py
uv run --env-file=.env python src/examples/langgraph/ex007.py
uv run --env-file=.env python src/examples/langgraph/ex008.py
```

## Observações

- Para sair dos chats interativos, use `q`, `quit` ou `exit`.
- `ex006.py` gera um `file.png` com o grafo em Mermaid PNG.
- Caso o modelo não seja carregado, verifique `OPENAI_API_KEY` e `OPENAI_MODEL` no `.env`.

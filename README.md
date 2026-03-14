# First Steps Lang Stack

Exemplos simples com LangChain + OpenAI usando `uv`.

## Requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Configuração

1. Crie o arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY="sua_chave_aqui"
OPENAI_MODEL="gpt-5-mini"
```

2. Sincronize as dependências do projeto:

```bash
uv sync
```

## Como executar

Para rodar o exemplo principal (`ex003.py`) carregando variáveis do `.env`:

```bash
uv run --env-file=".env" python src/examples/ex001.py
```

## Observações

- Para sair do chat interativo, digite: `exit`, `quit`, `bye` ou `q`.
- O arquivo `src/examples/ex003.py` usa `SystemMessage` + `HumanMessage` com `langchain`.

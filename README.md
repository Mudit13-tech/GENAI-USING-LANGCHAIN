# GenAI using LangChain

My notes and experiments from learning LangChain. Each script is a small,
standalone example of calling a chat model through LangChain's provider
integrations.

## What's here

| Script | What it does |
| --- | --- |
| `LLMS/llm_demo.py` | Calls Gemini (`gemini-3.5-flash-lite`) through `langchain-google-genai` |
| `ChatModels/cm_genai.py` | Uses a Qwen model hosted on Groq, via `langchain-groq`, at a high temperature |
| `ChatModels/deepseek.py` | Uses DeepSeek's chat model through `langchain-deepseek` |
| `ChatModels/huggingface.py` | Runs Zephyr 7B on a Hugging Face inference endpoint through `langchain-huggingface` |
| `ChatModels/test.py` | Checks the Groq key with the plain `groq` SDK, without LangChain |

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install langchain-groq langchain-deepseek groq   # used by the ChatModels scripts
cp .env.example .env
```

Fill in `.env` with keys for the providers you want to try. Each script only
needs its own key:

```
GEMINI_API_KEY=...
GROQ_API_KEY=...
DEEPSEEK_API_KEY=...
HUGGINGFACEHUB_ACCESS_TOKEN=...
```

Two of the integrations look for different names than the ones in
`.env.example`. `langchain-google-genai` looks for `GOOGLE_API_KEY`, and
`langchain-huggingface` looks for `HUGGINGFACEHUB_API_TOKEN`. If a script says
it can't find its key, add the variable under that name too.

## Run

```bash
python LLMS/llm_demo.py
python ChatModels/cm_genai.py
```

## Stack

Python, LangChain, python-dotenv, plus the Gemini, Groq, DeepSeek and
Hugging Face model APIs.

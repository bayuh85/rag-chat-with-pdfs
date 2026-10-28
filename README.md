# Chat With Your PDFs: a RAG app in Python

Code from the AtmoRouter video **"Chat With Your PDFs: Build a RAG App in Python (Free, Local, Any Model)"**.

`rag.py` is a complete retrieval-augmented generation (RAG) app in about 45 lines. It splits a PDF into chunks, embeds them locally with [fastembed](https://github.com/qdrant/fastembed) (`BAAI/bge-small-en-v1.5`, runs on your CPU), retrieves the closest chunks with NumPy, and asks any OpenAI-compatible chat model to answer **only** from those chunks, citing the page. If the PDF doesn't contain the answer, it says "I don't know."

## Files

| File | What it does |
|---|---|
| `rag.py` | The full RAG app |
| `rag_strict.py` | Same app with a stricter prompt |
| `ask_plain.py` | Asks the model with no PDF (to show it guessing) |
| `chunks.py` | Shows how the PDF is chunked |
| `embed_demo.py` | Shows embeddings and similarity scores |
| `make_pdf.py` | Rebuilds the demo PDF |
| `docs/kestrel_air_policies.pdf` | Demo PDF. Kestrel Air is a **fictional** airline. |

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Any OpenAI-compatible endpoint works.
# Free and local with Ollama:
export OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_API_KEY=ollama
export MODEL=qwen3:4b

python rag.py docs/kestrel_air_policies.pdf "Can I get a bereavement refund after my trip?"
```

### Use a bigger model

Point the same code at [AtmoRouter](https://atmorouter.dev): one API key for over 160 models, up to 95% off official pricing.

```bash
export OPENAI_BASE_URL=https://atmorouter.dev/v1
export OPENAI_API_KEY=your_atmorouter_key
export MODEL=<model id from atmorouter.dev>
```

## Links

- Discord: https://discord.gg/7jmCfCfKT
- X: https://x.com/sabrielatmojo
- Instagram: https://www.instagram.com/atmorouter/
- Threads: https://www.threads.com/@atmorouter.dev
- Facebook: https://web.facebook.com/atmorouter

MIT License.

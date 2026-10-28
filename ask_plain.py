# Ask the model directly: no documents, no RAG.
import os, sys
from openai import OpenAI
client = OpenAI()  # reads OPENAI_BASE_URL + OPENAI_API_KEY
MODEL = os.environ["MODEL"]
extra = {"reasoning_effort": "none"} if MODEL.startswith("qwen3") else {}
reply = client.chat.completions.create(model=MODEL, temperature=0, **extra,
    messages=[{"role": "system", "content": "Answer in 2-3 sentences."},
              {"role": "user", "content": sys.argv[1]}])
print(reply.choices[0].message.content.strip())

# Chat with your PDF: a complete RAG app in ~45 lines.
import os, sys
import numpy as np
from pypdf import PdfReader
from fastembed import TextEmbedding
from openai import OpenAI

client = OpenAI()  # reads OPENAI_BASE_URL + OPENAI_API_KEY
MODEL = os.environ["MODEL"]
embedder = TextEmbedding("BAAI/bge-small-en-v1.5")

# 1. Load + chunk: split every page into ~600-character pieces, remember the page.
def load_chunks(path, size=600, overlap=100):
    chunks = []
    for page_no, page in enumerate(PdfReader(path).pages, start=1):
        text = " ".join(page.extract_text().split())
        for start in range(0, max(len(text) - overlap, 1), size - overlap):
            chunks.append({"page": page_no, "text": text[start:start + size]})
    return chunks

# 2. Embed every chunk once: text -> 384 numbers.
chunks = load_chunks(sys.argv[1])
vectors = np.array(list(embedder.embed([c["text"] for c in chunks])))
print(f"indexed {len(chunks)} chunks from {sys.argv[1]}")

# 3. Retrieve: embed the question, keep the 3 closest chunks.
def retrieve(question, k=3):
    q = next(iter(embedder.embed([question])))
    best = np.argsort(vectors @ q)[::-1][:k]
    return [(float(vectors[i] @ q), chunks[i]) for i in best]

# 4. Generate: paste the chunks into the prompt and ask the model.
def answer(question):
    hits = retrieve(question)
    for score, c in hits:
        print(f"  [{score:.2f}] page {c['page']}: {c['text'][:70]}...")
    context = "\n\n".join(f"[page {c['page']}] {c['text']}" for _, c in hits)
    extra = {"reasoning_effort": "none"} if MODEL.startswith("qwen3") else {}
    reply = client.chat.completions.create(model=MODEL, temperature=0, **extra, messages=[
        {"role": "system", "content": "Use only the context below to answer. Cite the page like [page 2]. "
                                      "If the context does not contain the answer, reply: I don't know.\n\n" + context},
        {"role": "user", "content": question}])
    return reply.choices[0].message.content.strip()

for question in sys.argv[2:]:
    print(f"\nQ: {question}\nA: {answer(question)}")

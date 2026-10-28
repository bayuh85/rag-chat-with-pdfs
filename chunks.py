# Peek at the chunks: same chunking code as rag.py.
import sys
from pypdf import PdfReader
def load_chunks(path, size=600, overlap=100):
    chunks = []
    for page_no, page in enumerate(PdfReader(path).pages, start=1):
        text = " ".join(page.extract_text().split())
        for start in range(0, max(len(text) - overlap, 1), size - overlap):
            chunks.append({"page": page_no, "text": text[start:start + size]})
    return chunks
chunks = load_chunks(sys.argv[1])
print(f"{len(chunks)} chunks\n")
for i, c in enumerate(chunks):
    print(f"#{i} page {c['page']} ({len(c['text'])} chars): {c['text'][:60]}...{c['text'][-25:]}")

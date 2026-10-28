# Embeddings: text -> a list of numbers. Similar meaning -> similar numbers.
import sys
import numpy as np
from fastembed import TextEmbedding
embedder = TextEmbedding("BAAI/bge-small-en-v1.5")
question = "Is my puppy allowed on board?"
texts = ["Small cats and dogs may travel in the cabin if the animal and its carrier weigh no more than 7 kg.",
         "Extra bags cost $45 each when added online and $70 at the airport.",
         "Wi-Fi is free for messaging on all aircraft.",
         "The cat sat on the mat."]
q, *vecs = list(embedder.embed([question] + texts))
print(f"question: {question!r}")
print(f"vector: {len(q)} numbers -> [{', '.join(f'{x:+.3f}' for x in q[:5])}, ...]\n")
for t, v in sorted(zip(texts, vecs), key=lambda p: -float(p[1] @ q)):
    print(f"{float(v @ q):.2f}  {t}")

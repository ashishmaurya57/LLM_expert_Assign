from app.embedding import embed_text
from app.ingestion import index, doc_chunks
import numpy as np

def retrieve_similar_chunks(query, top_k=5):
    query_embedding = embed_text([query])[0]
    D, I = index.search(np.array([query_embedding]).astype("float32"), top_k)
    return [doc_chunks[i] for i in I[0]]

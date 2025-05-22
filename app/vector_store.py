from langchain_community.vectorstores import FAISS
from app.embedding import get_embeddings
import os

def save_to_vector_store(chunks, index_name: str):
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embedding=embeddings)
    path = f"data/{index_name}"
    os.makedirs(path, exist_ok=True)
    vector_store.save_local(path)
    return path

def load_vector_store(index_name: str):
    embeddings = get_embeddings()
    return FAISS.load_local(f"data/{index_name}", embeddings, allow_dangerous_deserialization=True)

import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"
DB_URL = os.getenv("DATABASE_URL", "sqlite:///./ragdb.sqlite3")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
VECTOR_DB_PATH = "vectorstore/faiss.index"

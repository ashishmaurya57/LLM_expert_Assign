from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL_NAME

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def embed_text(texts):
    return model.encode(texts, convert_to_numpy=True)

import os
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import CHUNK_SIZE, CHUNK_OVERLAP
from app.models import SessionLocal, DocumentMetadata
from app.utils import read_pdf_text
from app.embedding import embed_text
from sqlalchemy.exc import IntegrityError

index = faiss.IndexFlatL2(384)
doc_chunks = []

def ingest_pdf(file_path):
    text, page_count = read_pdf_text(file_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_text(text)

    embeddings = embed_text(chunks)
    index.add(np.array(embeddings).astype("float32"))
    doc_chunks.extend(chunks)

    db = SessionLocal()
    try:
        db.add(DocumentMetadata(filename=os.path.basename(file_path), pages=page_count))
        db.commit()
    except IntegrityError:
        db.rollback()
    db.close()

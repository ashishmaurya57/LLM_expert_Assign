import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.models import Base, engine, SessionLocal, DocumentMetadata
from app.ingestion import ingest_pdf
from app.retrieval import retrieve_similar_chunks
from app.llm import generate_response

app = FastAPI()

Base.metadata.create_all(bind=engine)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "RAG API is working"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    ingest_pdf(file_path)
    return {"message": f"{file.filename} uploaded and processed."}

@app.post("/query/")
async def ask_question(query: str = Form(...)):
    chunks = retrieve_similar_chunks(query)
    response = generate_response(query, chunks)
    return {"answer": response}

@app.get("/metadata/")
def get_metadata():
    db = SessionLocal()
    docs = db.query(DocumentMetadata).all()
    return [{"filename": doc.filename, "pages": doc.pages} for doc in docs]

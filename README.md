- 
- Upload up to 20 PDFs
- Chunk + Embed using HuggingFace
- Store in FAISS Vector DB
- Ask contextual questions using Groq LLM
- REST API using FastAPI
- Fully containerized using Docker

## setup
- Install reuirements.txt using "pip install -r requirements.txt". It contains all the dependency and libraries.

## Start the server with:
- uvicorn app.main:app --reload
## Fast Api - Swagger
- http://127.0.0.1:8000/docs
- This contains upload, get, query and metadata, where we can check aor api and working.
-Provides RESTful endpoints for:

   /upload/ – Upload and process PDF documents.

   /query/ – Ask a question and get an answer.

  /metadata/ – View uploaded document metadata.

## Frontend server
- Run using -> streamlit run rag_frontend.py 

.env -> Contains all the api key of model

## Docker
 -- Run docker-compose up --build
 - It contains code to automatically download all the requirements 

## Upload folder
 It contains all the uploaded pdf. Query can be asked from any pdf.

## Databse
- Uses Sqlite for storing pdfs


## 🚀 Getting Started
### 1. Clone + Set Environment
```bash
git clone -  https://github.com/ashishmaurya57/LLM_expert_Assignment.git
cp .env.example .env




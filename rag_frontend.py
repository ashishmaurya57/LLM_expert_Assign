import streamlit as st
import requests

st.set_page_config(page_title="RAG PDF QA", layout="centered")
st.title("📚 PDF Q&A Assistant")

# Backend URL
import os
BACKEND_URL = "http://localhost:8000"

# --- Upload PDF ---
st.header("1. Upload a PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Uploading and processing..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post(f"{BACKEND_URL}/upload/", files=files)

        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to upload PDF")

# --- Ask a Question ---
st.header("2. Ask a Question")
query = st.text_input("Enter your question:")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(f"{BACKEND_URL}/query/", data={"query": query})
            if response.status_code == 200:
                st.success("Answer:")
                st.write(response.json()["answer"])
            else:
                st.error("Failed to get a response from the backend.")

# --- Show Metadata ---
st.header("📄 Uploaded Document Metadata")
if st.button("Refresh Metadata"):
    meta = requests.get(f"{BACKEND_URL}/metadata/")
    if meta.status_code == 200:
        for doc in meta.json():
            st.write(f"📘 `{doc['filename']}` - {doc['pages']} page(s)")
    else:
        st.error("Could not fetch metadata.")

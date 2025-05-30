from PyPDF2 import PdfReader

def read_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text, len(reader.pages)

import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    """Extracts text from a PDF file using PyMuPDF."""
    text = ""
    with fitz.open(path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text.strip()

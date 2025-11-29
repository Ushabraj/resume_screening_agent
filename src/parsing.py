# parsing.py
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
from docx import Document  # for .docx files

def extract_text_from_pdf(path):
    """
    Extract text from PDF (digital or scanned)
    """
    text = ""
    # Try digital PDF first
    try:
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print("Digital PDF extraction error:", e)

    text = text.strip()

    # If no text, use OCR
    if len(text) == 0:
        try:
            print("No digital text found. Using OCR...")
            pages = convert_from_path(path)
            for page in pages:
                text += pytesseract.image_to_string(page)
        except Exception as e:
            print("OCR PDF extraction error:", e)

    return text.strip()


def extract_text_from_docx(path):
    """
    Extract text from a Word (.docx) file
    """
    try:
        doc = Document(path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print("DOCX extraction error:", e)
        return ""


def normalize_text(text):
    """
    Simple text normalization: lowercase and strip
    """
    return text.lower().strip()

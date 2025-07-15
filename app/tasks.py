import io

import pdf2image
import pytesseract
from celery import Celery
from PIL import Image

from app.settings import Settings

settings = Settings()
celery_app = Celery(
    name=settings.app_name,
    broker=settings.broker_url,
    backend=settings.backend_url,
)


@celery_app.task
def process_ocr(content_type: str, file_bytes: bytes):
    """
    Celery task to extract text from an image or PDF file.

    Args:
        content_type: MIME type of the file (e.g., 'application/pdf', 'image/png')
        file_bytes: Raw file content

    Returns:
        Extracted text as a string
    """
    if content_type == "application/pdf":
        return _extract_text_from_pdf(file_bytes)
    else:
        return _extract_text_from_image(file_bytes)


def _extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text from a PDF by converting pages to images and running OCR.

    Args:
        pdf_bytes: Raw PDF content

    Returns:
        Combined text extracted from all pages
    """
    images = pdf2image.convert_from_bytes(pdf_bytes)
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"

    return full_text


def _extract_text_from_image(file_bytes: bytes) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Args:
        file_bytes: Raw image content

    Returns:
        Extracted text
    """
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image)
    return text

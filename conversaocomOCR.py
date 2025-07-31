import pdfplumber
import pytesseract
from PIL import Image, ImageDraw


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_ocr_com_risco(pdf_path, page_number=0):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        im = page.to_image(resolution=300)
        pil_image = im.original

        
        gray = pil_image.convert("L")
        texto = pytesseract.image_to_string(gray, lang='por')

        return texto


pdf_path = "Anatel - Ato nº 2436, de 7 de março de 2023.pdf"
texto = extrair_texto_ocr_com_risco(pdf_path, page_number=0)

with open("ocr_extraido.txt", "w", encoding="utf-8") as f:
    f.write(texto)

import pdfplumber
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_ocr_completo(pdf_path):
    texto_completo = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            im = page.to_image(resolution=300)
            pil_image = im.original

            gray = pil_image.convert("L")
            threshold = 150
            binarized = gray.point(lambda p: 255 if p > threshold else 0)

            texto = pytesseract.image_to_string(binarized, lang='por', config='--psm 6')
            texto_completo += texto + "\n\n"  # separa páginas com linhas em branco

    return texto_completo

pdf_path = "L10973.pdf"
texto = extrair_texto_ocr_completo(pdf_path)

with open("ocr_extraido.txt", "w", encoding="utf-8") as f:
    f.write(texto)

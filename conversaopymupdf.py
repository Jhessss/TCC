import fitz  # PyMuPDF

def extrair_texto_pdf(pdf_path, com_riscado=True):
    doc = fitz.open(pdf_path)
    texto_com_riscado = ""
    texto_sem_riscado = ""

    for page in doc:
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    texto = span["text"]
                    is_strike = span.get("strike", False)

                    if is_strike:
                        if com_riscado:
                            texto_com_riscado += f"[RISCADO]{texto}[/RISCADO]"
                        
                    else:
                        texto_com_riscado += texto
                        texto_sem_riscado += texto

                texto_com_riscado += "\n"
                texto_sem_riscado += "\n"

    return texto_com_riscado, texto_sem_riscado



pdf_path = r'D:\temp\UnB25\UnB\TCC\codigosTCC\Anatel - Ato nº 2436, de 7 de março de 2023.pdf'
com, sem = extrair_texto_pdf(pdf_path)

# Salvar os arquivos .txt
with open("com_riscado.txt", "w", encoding="utf-8") as f:
    f.write(com)

with open("sem_riscado.txt", "w", encoding="utf-8") as f:
    f.write(sem)

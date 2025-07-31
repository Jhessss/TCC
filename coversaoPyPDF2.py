import PyPDF2

caminho_pdf = r'D:\temp\UnB25\UnB\TCC\codigosTCC\Anatel - Ato nº 2436, de 7 de março de 2023.pdf'

caminho_txt = 'saidaPyPDF2.txt'

with open(caminho_pdf, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfReader(arquivo_pdf)
    texto_extraido = ''

    for pagina in leitor.pages:
        texto_extraido += pagina.extract_text() or ''


with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
    arquivo_txt.write(texto_extraido)

print(f'Texto extraído com sucesso para "{caminho_txt}"!')

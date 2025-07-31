import pdfplumber
import re


caminho_pdf = r'D:\temp\UnB25\UnB\TCC\codigosTCC\Anatel - Ato nº 2436, de 7 de março de 2023.pdf'


caminho_txt = 'saidapdfplumber.txt'


def limpar_texto(texto):
   
    texto = re.sub(r'[ \t]+', ' ', texto)
    texto = re.sub(r'\n+', '\n', texto)
    texto = '\n'.join(linha.strip() for linha in texto.splitlines())
    return texto.strip()


texto_extraido = ''
with pdfplumber.open(caminho_pdf) as pdf:
    for pagina in pdf.pages:
        texto_pagina = pagina.extract_text()
        if texto_pagina:
            texto_extraido += texto_pagina + '\n'


texto_limpo = limpar_texto(texto_extraido)


with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
    arquivo_txt.write(texto_limpo)

print(f'Texto extraído com sucesso para "{caminho_txt}"!')

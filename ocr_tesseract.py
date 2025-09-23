import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def pegar_IMG(pasta: str, extensoes=(".png", ".jpg", ".jpeg", ".tiff", ".pdf")):
    arquivos_img = []
    for dado in os.listdir(pasta):
        caminho = os.path.join(pasta, dado)
        if os.path.isfile(caminho) and caminho.lower().endswith(extensoes):
            arquivos_img.append(caminho)
        elif os.path.isdir(caminho):
            arquivos_img += pegar_IMG(caminho, extensoes)
    return arquivos_img        



def ler_imagem(lista_arquivos):
    textos = []
    for caminho in lista_arquivos:
        try:
            if caminho.lower().endswith('.pdf'):
                paginas = convert_from_path(caminho)
                texto = "\n".join(pytesseract.image_to_string(p) for p in paginas)
            else:
                with Image.open(caminho) as im:
                    texto = pytesseract.image_to_string(im)
            textos.append(texto)
        except Exception as e:
            textos.append(f"Erro ao processar {caminho}: {e}")
    return textos

def salvar_txt(lista_arquivos: list[str], textos: list[str], caminho_textos: str):
    if len(lista_arquivos) != len(textos):
        raise ValueError('O tamanho dos pdfs e dos textos devem ser iguais.')
    os.makedirs(caminho_textos, exist_ok=True)

    for img, texto in zip(lista_arquivos, textos):
        nome = os.path.basename(img)                 # pega só o nome do arquivo
        base, _ = os.path.splitext(nome)             # separa nome e extensão
        caminho = os.path.join(caminho_textos, base + '.txt')  # força .txt
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(texto)

  

lista_arquivos = pegar_IMG("PDF_img")
texto_imagem = ler_imagem(lista_arquivos)
salvar_txt(lista_arquivos, texto_imagem, "textos-IMG_txt")
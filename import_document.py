import os 
from pypdf import PdfReader


def pegar_PDF(pasta:str):
    arquivos_pdf = []
    for dado in os.listdir(pasta):
        dado = os.path.join(pasta, dado)
        if os.path.isfile(dado):
            if dado.lower().endswith(".pdf"):
                arquivos_pdf.append(dado)
        else:
            arquivos_pdf += pegar_PDF(dado)
    return arquivos_pdf        
                
def ler_arquivos(arquivos_pdf):
    lista_de_textos = []
    for pdf in arquivos_pdf:
        textos = ''
        reader = PdfReader(pdf)
        for pagina in reader.pages:
            textos += pagina.extract_text()
        lista_de_textos.append(textos)
    return lista_de_textos

def salvar_txt(pdfs: list[str], textos: list[str], caminho_textos):
    if len(pdfs) != len(textos):
        raise ValueError('O tamanho dos pdfs e dos texto devem ser iguais.')
    os.makedirs(caminho_textos, exist_ok=True)
    for pdf, texto in zip(pdfs, textos):
        pdf = pdf.split('\\')[-1]
        caminho = os.path.join(caminho_textos, pdf.lower().replace('pdf', 'txt'))
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(texto)

## main ():
pdfs = pegar_PDF("docs")
print(ler_arquivos(pdfs))

lista = ler_arquivos(pdfs)
salvar_txt(pdfs, lista, "textos_txt")#o último parâmetro é o nome da pasta em que colocaremos o arquivo


        
        

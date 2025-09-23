import os ##serve para interagir com o sistema operacional, listando pastas e arquivos.
from pypdf import PdfReader ##Usada para ler a menipular arquivos pdf. Usarei para ler os pdfs e transformar num txt

def pegar_pdf(pasta:str): ##variável parâmerto e sua tipagem.
    lista_pdfs = [] #lista para armazenar todos os caminhos dos pdfs de alguma pasta
    for dado in os.listdir(pasta):
        dado = os.path.join(pasta, dado) #junta dois caminhos para construir o caminho de cada pdf
        if os.path.isfile(dado): #verifica se dado é uma pasta ou um arquivo
            if dado.lower().endswith(".pdf"): #verifica se o arquivo é pdf
                lista_pdfs.append(dado) #adiciona dado a lista de pdfs da pasta
            else:
                lista_pdfs += pegar_pdf(dado) #se ele encontrar uma pasta, vai percorrer ela verificando se existe mais pdfs
    return lista_pdfs

def ler_arquivo(lista_pdfs):
    lista_textos = [] #salvará o texto inteiro em uma lista
    for pdf in lista_pdfs: #Percorre todos os pdfs da lista de pdfs
        texto = '' #cria uma string para armazenar o texto de cada página
        reader = PdfReader(pdf) #'abre o pdf'
        for pages in reader.pages:#percorre todas as páginas no pdf 
            texto += pages.extract_text()#extrai o texto e salva na string
        lista_textos.append(texto) #adiciona o conteúdo de cada página na lista
    return lista_textos

def salvar_txt(pfds:list[str], textos:list[str], caminho):
    
    

from import_document import pegar_PDF, ler_arquivos, salvar_txt
import gdown

folder_url = "https://drive.google.com/drive/folders/1UODdhxX-YIRO2PMnb9u9qacakoE_gjZh?usp=sharing"

gdown.download_folder(folder_url, output="temp_drive", quiet=False, use_cookies=False)

pdfs = pegar_PDF("temp_drive")
textos = ler_arquivos(pdfs)
salvar_txt(pdfs, textos, "textos_txt")

### baixa todos os arquivos da pasta do drive e converte de pdf para txt
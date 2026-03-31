import os
import shutil
# Defina o caminho da pasta que quer organizar
caminho = "C:/Users/Vinny/Downloads"
    
# Mapeamento de extensões para pastas
diretorios = {
        "Imagens": [".jpg", ".jpeg", ".png"],
        "Documentos": [".pdf", ".docx", ".txt"],
        "Planilhas": [".xlsx", ".csv"]
    }

for arquivo in os.listdir(caminho):
    nome, extensao = os.path.splitext(arquivo)
    for pasta, extensoes in diretorios.items():
        if extensao.lower() in extensoes:
            caminho_pasta = os.path.join(caminho, pasta)
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)
            shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho_pasta))
            print(f"Movido: {arquivo} -> {pasta}")
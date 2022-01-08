import os, shutil

caminho_original = '/home/lara/Downloads'
caminho_novo = '/home/lara/Downloads/teste'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta: {caminho_novo} já existe')
"""
# Copiar ou mover os arquivos
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_path = os.path.join(root, file)
        new_path = os.path.join(caminho_novo, file)
        
        if '.pdf' in file:
            shutil.copy(old_path, new_path)
            print(f'{file} copiado com sucesso')
"""
# Apagar os arquivos       
for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_path = os.path.join(root, file)
        new_path = os.path.join(caminho_novo, file)
        
        if '.pdf' in file:
            os.remove(new_path)
            print(f'{file} apagado com sucesso')
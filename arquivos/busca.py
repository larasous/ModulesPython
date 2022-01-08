import os
from utils import format_tam

caminho = input('Digite o caminho: ')
termo = input('Digite o termo: ')

cont = 0
for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arq, ext_arq = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arq)
                print('Extensão:', ext_arq)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', format_tam(tamanho))
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido:', e)
            
print(f'{cont} arquivo(s) encontrado(s)')
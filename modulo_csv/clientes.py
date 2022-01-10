"""
CSV - Comma Separated Values (Valores separados por vírgula)
É um formato de dados bastante utilizados em tabelas (Excel, Google Sheet, etc),
bases de dados, clientes de email, etc...
"""
import csv

with open('modulo_csv/clientes.csv', 'r') as file:
    # retorna um iterador
    # dados = csv.reader(file) # ler o arquivo
    
    dados = [x for x in csv.DictReader(file)] # formato de dicionário
    
with open('modulo_csv/clientes2.csv', 'w') as file:
    escrever = csv.writer(
        file, 
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
        )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escrever.writerow(
           [ 
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
            ]
        )

    for dado in dados:
        escrever.writerow(
           [ 
            dado['Nome'], 
            dado['Sobrenome'], 
            dado['Email'], 
            dado['Telefone']
            ]
        )
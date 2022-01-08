from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8') # alterando o idioma da data

d1 = datetime.now()
mes_at = int(d1.strftime('%m'))
fmt1 = d1.strftime("%A, %d de %B de %Y")
fmt2 = d1.strftime("%d/%m/%Y %H:%M:%S")

print(fmt1)
print(fmt2)

print(mes_at, mdays[mes_at]) # Mês - Qtd de dias


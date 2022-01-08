"""
Trabalhando com datas e horas
- https://docs.python.org/2/library/datetime.html
"""
from datetime import datetime, timedelta

# ano, mes, dia, hora, minutos, segundos
data = datetime(2022, 4, 6, 12, 30, 15)
print(data.strftime("%d/%m/%Y %H:%M:%S"))

t = data.timestamp()

data2 = datetime.strptime('14/01/2022', '%d/%m/%Y')

data3 = datetime.fromtimestamp(t)
data2 = data2 + timedelta(days=6)

print(data2.strftime("%d/%m/%Y"))
print(data3.strftime("%d/%m/%Y"))
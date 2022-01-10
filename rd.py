import random
import string

# Gera um inteiro entre A e B
inteiro = random.randint(10, 20)

# Gera um numero aleatorio usando a função range()
inteiro2 = random.randrange(900, 1000, 10)

# Gera um float entre A e B
flutuante = random.uniform(10, 20)

# Gera um float entre 0 e 1
flutuante2 = random.random()

lista = ['Ana', 'Maria', 'João', 'Daniel', 'Luiz']

# Seleciona um item da lista
sorteio = random.choice(lista) 

# Seleciona k itens da lista, pode pegar igual
sorteio2 = random.choices(lista, k=2)

# Mesma função do choices, porém, não repete os itens
sorteio3 = random.sample(lista, 2) 

random.shuffle(lista) # Embaralhar a lista

# Gerar senha aleatoria
letras = string.ascii_letters # Maiúsculas e minúsculas
digitos = string.digits
caracteres = '!@#$%&*_-.'
geral = letras + digitos + caracteres

print()
for i in range(10):
    senha = ''.join(random.choices(geral, k=10))

    print(f'{i} - {senha}')
print()

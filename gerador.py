import random
import string


senha = ''
symbols = '#@&!'

group = string.ascii_letters + string.digits + symbols

size = int(input('Escolha um tamano: '))

for p in range(size):
    senha += random.choice(group)

print(senha)
import random
import string


senha = ''
symbols = '#@&!'
numbers = '0123456789'

group = string.ascii_letters + numbers + symbols

size = int(input('Escolha um tamano: '))

for p in range(size):
    senha += random.choice(group)

print(senha)
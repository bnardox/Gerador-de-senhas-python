import random
import string
from time import sleep
import os


#Definindo algumas variavies importantes
senha = ''
symbols = '#@&!'

#Concatenando as letras maiusculas e minusculas e números
group = string.ascii_letters + string.digits + symbols

print()
print('------------------------------')
print(f'-  Gerador de senhas PYTHON  -')
print('------------------------------\n')

while True:
    try:
        #Input receber o tamanho da senha
        size = int(input('Escolha um tamanho: '))
        print()
        break
    except ValueError:
        print('Digite um NÚMERO!\n')
        sleep(0.6)
        continue
sleep(1)
print('Gerando senha...', end=' ')

#Gerando a senha de acordo com o tamanho
for p in range(size):
    senha += random.choice(group)
print('Senha gerada!\n')
#Mostrando a senha
sleep(0.8)
print(f'A senha gerada foi: {senha}')
sleep(1.5)
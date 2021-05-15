import random
import string


#Definindo algumas variavies importantes
senha = ''
symbols = '#@&!'

#Concatenando as letras maiusculas e minusculas e números
group = string.ascii_letters + string.digits + symbols

#Input receber o tamanho da senha
size = int(input('Escolha um tamano: '))

#Gerando a senha de acordo com o tamanho
for p in range(size):
    senha += random.choice(group)

#Mostrando a senha
print(senha)
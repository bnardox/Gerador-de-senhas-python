import random
import string
from time import sleep


#Definindo algumas variavies importantes
senha = ''
symbols = '@&!'

#Concatenando as letras maiusculas e minusculas e números
group = string.ascii_letters + string.digits + symbols

#Menu
print()
print('------------------------------')
print(f'-  Gerador de senhas PYTHON  -')
print('------------------------------\n')
sleep(0.5)

while True:
    try:
        #Input receber o tamanho da senha
        size = int(input('Escolha um tamanho: '))
        if size == 0:
            print('Saindo...')
            sleep(0.4)
            exit()
            
        elif size > 1000: #Não deixa gerar senhas acima de 1000
            print('Não foi possivel gerar esse valor!')
            continue

        else:
            print()
            break

    except ValueError: #Caso o usuario digite algo que não for um número
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
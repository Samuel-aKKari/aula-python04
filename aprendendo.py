#1
'''
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

if a > b:
    print(f'{a} é o maior')
else:
    print(f'{b} é o maior')
'''
from traceback import print_tb

#2
'''
ano = int(input('Em que ano você nasceu?'))
idade = 2025 - ano

if idade < 16:
    print(f'Você não pode votar esse ano!')
elif idade < 18 or idade >= 70:
    print(f'Seu voto é opcional')
else:
    print('Tem que votar e fazer o L clt fudido')
'''

#3
'''
senha_cadastrada = "1234"
senha_fornecida = (input("Qual é a senha?\n->"))

if senha_fornecida == senha_cadastrada:
    print("Acesso liberado!!!")
else:
    print("SAI HAKU")
'''

#4
'''
quantidade = int(input('Diga o numero de maças: '))
valor = 0.25

if quantidade < 12:
    valor = 0.30
total = quantidade * valor
print(f'Você gastará R${total:.2f} por {quantidade} maças, por ser R${valor} a cada maças.')
'''

#6
'''
genero = input('Diga masculino ou feminino:')
altura = float(input('Diga sua altura:'))
peso = (62.1*altura) - 44.7
if genero == 'masculino':
    peso = (72.7*altura) - 58
    print(f'O seu peso ideal pro {genero} de acordo com a sua altura de {altura} é de {peso:.2f}')
'''

#7,8
'''
lados = int(input('Quantos lados tem a sua figura:\n->'))
if lados < 3:
    print('Não é um poligono')
elif lados > 5:
    print('Poligono nao encontrado!')
else:
    medida = int(input('Qual a medida da figura:\n->'))
    perimetro = lados * medida
    if lados == 3:
        forma = 'triangulo'
    elif lados == 4:
        forma = 'quadrado'
    else:
        forma = 'pentágono'
    print(f'É um {forma} de perimetro {perimetro}')
'''

#10
'''
a = int(input('Diga o primeiro lado: '))
b = int(input('Agora diga o segundo lado: '))
c = int(input('E agora o terceiro lado: '))

if a == b and a == c:
    print('Equilatero')
elif a == b or a == c or c == b:
    print('Isósceles')
else:
    print('Escaleno')
'''

#11
'''
a = int(input('Diga o primeiro lado: '))
b = int(input('Agora diga o segundo lado: '))
c = int(input('E agora o terceiro lado: '))

if a+b+c == 180:
    if a == 90 or b == 90 or c == 90:
        print('Triangulo reto')
    elif a > 90 or b > 90 or c > 90:
        print('Triangulo obtuso')
    else:
        print('Triangulo agudo')
else:
    print('Não é um triangulo!!!')
'''

#9
'''
a = int(input('Diga o primeiro numero: '))
b = int(input('Agora diga o segundo numero: '))
c = int(input('E agora o terceiro numero: '))

if a>b and a>c:
    aux = a
    a = c
    c = aux
elif b>c:
    aux = c
    c = b
    b = aux
if a>b:
    aux = a
    a = b
    a = aux
print(a, b, c)
'''

#5
'''
a = int(input('Diga o primeiro numero: '))
b = int(input('Agora diga o segundo numero: '))
c = int(input('E agora o terceiro numero: '))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
meio = a + b + c - menor - maior
print(menor, meio, maior)
'''


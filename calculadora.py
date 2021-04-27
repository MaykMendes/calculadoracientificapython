from time import sleep
from math import sqrt


def soma():
    n1 = int(input(': '))
    n2 = int(input(f'{n1} + '))

    print(f'{n1} + {n2} = {n1 + n2}')


def subtrair():
    n1 = int(input(': '))
    n2 = int(input(f'{n1} - '))

    print(f'{n1} - {n2} = {n1 - n2}')


def multiplicar():
    n1 = int(input(': '))
    n2 = int(input(f'{n1} x '))

    print(f'{n1} x {n2} = {n1 * n2}')


def dividir():
    n1 = int(input(': '))
    n2 = int(input(f'{n1} ÷ '))
    divisão = n1 / n2

    print(f'{n1} / {n2} = {divisão:.1f}')


def equação_de_2º_grau():
    while True:
        # Recebendo dados do usuário
        try:
            a = int(input("Digite o valor A: "))
        except ValueError:
            a = int(input("Digite Apenas numeros inteiros: "))
        try:
            b = int(input("Digite o valor B: "))
        except ValueError:
            b = int(input("Digite apenas números inteiros: "))
        try:
            c = int(input("Digite o valor C: "))
        except ValueError:
            c = int(input("Digite apenas números inteiros: "))
        print("CALCULANDO...")
        sleep(3)
        # Calculando
        if a == 0:
            print("\033[1;31mSeus valores não se encaixam no perfil de uma equação de segundo grau\033[m")
            break

        delta = pow(b, 2) - (4*a*c)
        if delta < 0:
            print("\033[1;32mNão existe raiz!\033[m")
            break

        x = (-b) + sqrt(delta) / 2 * a
        x2 = (-b) - sqrt(delta) / 2 * a

        raiz1 = x / (2 * a)
        raiz2 = x2 / (2 * a)

        # Analisando o resultado e retornando a resposta

        if delta == 0:
            print(f"\033[1;32mRaiz unica: {raiz1}\033[m")
            break

        elif delta > 0:
            print(f"\033[1;32mAs duas raizes A e B são respectivamente: {raiz1} e {raiz2}\033[m")
            break



def retangulo():
    print('Formúla A = b x h')
    c1 = int(input('b = '))
    c2 = int(input('h = '))
    print(f'A = {c1} m x {c2} m = {c1 * c2} m²')


def triangulo():
    print('Formúla A = b x h / 2')
    c1 = int(input('b = '))
    c2 = int(input('h = '))
    print(f'A = {c1} m x {c2} m = {c1 * c2 / 2} m²')


def circulo():
    print('Formúla A = π x r²')
    c1 = int(input('r² = '))
    print(f'A = 3,14 x {c1}² = {3.14 * (c1 ** 2)} m²')
    

def juros_simples():
    c = float(input("Capital emprestado R$: "))
    i = float(input("Taxa de juros do periodo: "))
    t = float(input("Tempo(meses): "))

    J = (c * i * t) / 100

    print(f"O valor dos juros será de R${J:.2f}")
    print(f"O total do montante é de R${c + J:.2f}")



# loop
while True:

    # select option
    select = input("""Escolha qual conta deseja fazer
    1 = Soma
    2 = Subtração
    3 = Multiplicação
    4 = Divisão
    5 = Equação de Segundo Grau
    6 = Cálculos de Áreas
    7 = Cálculo de Juros simples
    Sua escolha >> """)

    if select == '1':
        soma()

        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

    elif select == '2':
        subtrair()

        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

    elif select == '3':
        multiplicar()

        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

    elif select == '4':
        dividir()

        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

    elif select == '5':
        equação_de_2º_grau()

        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

    elif select == '6':
        select2 = input('''Escolha qual cálculo de área deseja fazer
       1 = Área de rentângulo
       2 = Área de Triângulo
       3 = Área do Circulo
       Sua escolha >> ''')

        if select2 == '1':
            retangulo()

            cont = input("Deseja realizar outra operação?[S/N]:").upper()
            if cont == 'S':
                continue
            else:
                break

        elif select2 == '2':
            triangulo()

            cont = input("Deseja realizar outra operação?[S/N]:").upper()
            if cont == 'S':
                continue
            else:
                break

        elif select2 == '3':
            circulo()

            cont = input("Deseja realizar outra operação?[S/N]:").upper()
            if cont == 'S':
                continue
            else:
                break

        else:
            print('Caractere não reconhecida, tente novamente!')
                
    elif select == '7':
        juros_simples()
        
        cont = input("Deseja realizar outra operação?[S/N]:").upper()
        if cont == 'S':
            continue
        else:
            break

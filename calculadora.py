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

    print(f'{n1} x {n2} = {divisão:.1f}')


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
            continue

        
        delta = pow(b, 2) - (4*a*c)
        if delta < 0:
            print("\033[1;32mNão existe raiz!\033[m")
            cont = str(input("Deseja realizar outra equação?[S/N]:")).upper()
            if cont == "S":
                continue
            else:
                break

        x = (-b) + sqrt(delta) / 2 * a
        x2 = (-b) - sqrt(delta) / 2 * a

        raiz1 = x / (2 * a)
        raiz2 = x2 / (2 * a)

        # Analisando o resultado e retornando a resposta 

        if delta == 0:
            print(f"\033[1;32mRaiz unica: {raiz1}\033[m")

        elif delta > 0:
            print(f"\033[1;32mAs duas raizes A e B são respectivamente: {raiz1} e {raiz2}\033[m")

        cont = str(input("Deseja realizar outra equação?[S/N]:")).upper()
        if cont == "N":
            break

# loop
while True:

    # select option
    select = input("""Select a option(number) and write below
1 = Soma
2 = Dimuir
3 = Multiplicação
4 = Divisão 
5 = Equação de segundo grau
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



# loop
while True:

    # select option
    select = input("""Select a option(number) and write below
    1 = Soma
    2 = Dimuir
    3 = Multiplicação
    4 = Divisão 
    """)

    if select == '1':
        n1 = int(input('Escreva um número: '))
        n2 = int(input('Escreva outro número: '))
        soma = n1 + n2
        print(soma)

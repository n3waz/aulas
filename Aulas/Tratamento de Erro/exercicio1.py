import os
os.system('cls')

def raiz():
    while True:
        try:
            num = int(input("Digite um número: "))

            num_quadrado = num**(1/2)

            print(num_quadrado)

            break

        except ValueError:

            print("Digite um número inteiro numérico.")
            

raiz()

import os
os.system("cls")

valor = int(input(" Insira o valor do produto: "))

if valor == 0:
    print(f"R$0,00")
else:
    while valor >=1000:
        valor+=valor

        
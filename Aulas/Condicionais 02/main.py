import os
os.system("cls")

num1 = int(input("Digite o primeiro valor do intervalo: "))
num2 = int(input("Digite o primeiro valor do intervalo: "))
soma = 0
while num1<=num2:
    if num1%2==0:
        soma = soma + 1
    num1+= 1
    print(soma)




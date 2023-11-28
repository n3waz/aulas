import os
os.system ("cls")
soma = 0
while True:
    valor = float(input("Digite um valor: "))
    if valor<0:
        print("Valor Inválido")
    elif valor ==0:
        break
    else:
        soma+=valor
if soma>1000:
    soma*=0.9
print(soma)


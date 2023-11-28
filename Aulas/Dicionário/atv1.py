numeros = {}
num = int(input("Digite um número: "))

for i in range(num+1):
    numeros[i] = i*i #se o i está sendo iterado, então se põe o i para o dicionário, sendo o número de iterações o dicionario
print(numeros)
print(numeros.items())
print(numeros.keys())
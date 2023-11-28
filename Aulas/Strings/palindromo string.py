import os
os.system("cls")

frases = input("Insira a frase: ").lower() #Precisa por o lower ou o upper para ser considerado iguais

frases = "".join(frases.split())

if frases == frases[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
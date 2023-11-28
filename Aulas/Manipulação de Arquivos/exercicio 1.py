import os
os.system('cls')

dados = open('Atividades\Aulas\manipulacao.py\dados.txt', 'r', encoding='utf-8')

# for linha in dados:
#     print(linha.strip()) # tira os espaços em branco
#     print(len(linha.split())) # conta as palavras 
#     print(len(linha.strip())) # conta os caracteres

string = dados.read()
print(string)
print(len(string))
print(len(string.split()))

dados.close()


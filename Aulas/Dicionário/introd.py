#possui chave(key) e valor(value)
#sintaxe: {} ou dict()
#sintaxe quando o dicionario ja tem valores: dicionario = {'chave':valor}
#sintaxe de lista no dicionario: dicionario = {'chave':[valor1,valor2]}
#organização de dicionario:
#remover valores do dicionario: del dicionario("chave") deletar tudo
#manipular remoçao de valores: print(dicionario.pop("chave", "alterar mensagem de erro*"))
#tamanho do dicionario: verificar a qtd de itens no dicionario; len(dicionario)
import os
os.system("cls")

#dicionario = {"Maria":111111, "Pedro":222222}
#print(dicionario)
#dicionario["Maria"] = 333333
#print(dicionario)
#dicionario["João"] = 444444
#print(dicionario)

dicionario = {}
for i in range(3):
    nome= input("Digite o nome do contato: ")
    telefone = input(f"Digite o telefone de {nome}: ")

    dicionario[nome] = telefone

print(dicionario)
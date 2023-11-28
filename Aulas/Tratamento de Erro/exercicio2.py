import os
os.system('cls')

arquivo = open("C:/Users/SAMSUNG/Desktop/FUNDAMENTOS DA PROGRAMAÇÃO/Atividades/Aulas/tratamento_erro/arquivo.txt", 'r', encoding="utf-8")

transform = arquivo.read()
arquivo.close()
for i in transform:
    if i == 'a':     
        arquivo = open("C:/Users/SAMSUNG/Desktop/FUNDAMENTOS DA PROGRAMAÇÃO/Atividades/Aulas/tratamento_erro/arquivo.txt", 'a+', encoding="utf-8")
        transform.replace('a', 'A')
        arquivo.write(transform)
        print(arquivo)
        
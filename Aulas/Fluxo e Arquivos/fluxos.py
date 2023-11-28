import os 
os.system("cls")
nomes = [] # lista nome
idades = [] #lista idade

def armazenar_idades(): # função para armazenar nomes e idades
    while True: # loop infinito

        nome = (input("Digite o nome: ")) # input nome
        idade = (input("Digite a idade: ")) # input idade
       #============================================================= 
        if idade == '-1': # condição para parar o loop
            break # para o loop

       #=============================================================
        if nome == 'nome': # condição para não armazenar o nome nome
            continue # volta para o loop

       #============================================================= 
        nomes.append(nome) # adiciona o nome na lista nomes
        idades.append(idade) # adiciona a idade na lista idades

       #=============================================================
    print(nomes, idades) # printa as listas nomes e idades

armazenar_idades() # chama a função armazenar_idades
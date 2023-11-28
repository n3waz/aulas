import os
os.system("cls")
cardapio = {
    "coxinha":[5.00],
    "pastel":[4.00],
    "suco":[3.00],
    "bolo":[4.50]
}
while True: # loop infinito

    pergunta = input("[A]Adicionar [R]Remover [M]Modificar: ").upper() # .upper() para deixar tudo em maiúsculo

    if pergunta=='A': # se a resposta for A

        nome = input("Qual o nome do produto? ") # pergunta o nome do produto

        valor = float(input("Qual o valor do produto? ")) # pergunta o valor do produto

        cardapio[nome] = valor # adiciona o produto ao cardápio

    elif pergunta == 'R': # se a resposta for R

        nome = input("Quer remover algum produto?") # pergunta qual produto quer remover

        if cardapio.get(nome): # se o produto estiver no cardápio

            cardapio.pop(nome) # remove o produto

        else: # se não estiver no cardápio

            print("Erro.") # printa erro

    elif pergunta == 'M': # se a resposta for M

        nome = input("Gostaria de modificar qual produto?") # pergunta qual produto quer modificar

        valor = float(input(f"Qual novo valor para {nome}")) # pergunta o novo valor

        if cardapio.get(nome): # se o produto estiver no cardápio

            cardapio[nome] = valor # modifica o valor do produto

        else: # se não estiver no cardápio

            print("Nome inválido.") # printa erro

    else: # se a resposta não for A, R ou M

        print("Opção Inválida") # printa erro
    
    decisão = print(f"\nCardápio modificado:\n{cardapio}") # printa o cardápio modificado

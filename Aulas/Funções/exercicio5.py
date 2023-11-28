def soma(num_soma1, num_soma2):
    resultado = num_soma1+num_soma2
    return resultado

def subtracao(num_subtracao1, num_subtracao2):
    resultado = num_subtracao1-num_subtracao2
    return resultado

def multiplicacao(num_multiplicacao1, num_multiplicacao2):
    resultado = num_multiplicacao1*num_multiplicacao2
    return resultado

def divisao(num_divisao1, num_divisao2):
    if num_divisao1 > num_divisao2:
        resultado = num_divisao1/num_divisao2
    if num_divisao2 > num_divisao1:
        resultado = num_divisao2/num_divisao1
    return resultado

continuar = input("Deseja realizar uma operação [S] ou [N] ?")

while continuar == "S" or continuar =="s":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print("\n[A] Soma [B] Subtração [C] Multiplicação [D] Divisão")
    opcao = input("Escolha a opcão desejada: ").upper()

    if opcao == "A":
        print(soma(num1, num2))
    elif opcao == "B":
        print(subtracao(num1, num2))
    elif opcao == "C":
        print(multiplicacao(num1, num2))
    else:
        print(divisao(num1, num2))

    continuar = input("\nDeseja realizar outra operação? [S] ou [N]?").upper()
nota1 = int(input())
nota2 = int(input())

def status(s): 
    if s > 6:
        print("Aprovado")
    elif 4 < s < 6:
        print("Verificação Suplementar")
    else:
        print("Reprovado")


def calc(num1, num2):
    media = (num1+num2)/2 
    return media

media = calc(nota1, nota2)
status(media)



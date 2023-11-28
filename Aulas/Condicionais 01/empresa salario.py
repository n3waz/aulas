import os
os.system("cls")
from datetime import date

ano_atual = date.today().year
admissao = int(input("Há quantos anos você foi admitido na empresa? "))
salario_atual = float(input("Qual seu atual salário? "))
reajuste = int(input("Há quanto tempo foi seu último reajuste? "))

if (admissao - reajuste)>=2:
    if admissao - reajuste>10:
        salario = salario_atual*1.30
        print(f"Novo salário = {salario}")
    elif 5<=(admissao - reajuste)<=10:
        salario = salario_atual*1.20
        print(f"Novo salário = {salario}")
    elif (admissao - reajuste)<5:
        salario = salario_atual*1.1
        print(f"Novo salário = {salario}")
else:
    print("Não apto ao reajuste.")
    
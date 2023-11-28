consumo = int(input("Informe o valor do seu consumo de energia: "))

if consumo<=500:
    tarifa = consumo*0.02+5 
    print(f"Sua tarifa foi de {tarifa}")
elif 500<consumo>=1000:
    tarifa = (consumo*10)+5
    print(f"Sua tarifa foi de {tarifa}")
elif 1000<consumo:
    tarifa = (consumo*35)+5
    print(f"Sua tarifa foi de {tarifa}")
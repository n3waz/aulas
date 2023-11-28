level = int(input("Insira o level do choque: "))

if level >= 1 and level <=20:
    print(f"20+{level}³")

elif level >=21 and level <=40:
    print(f"8000+{level-10}²")

elif level >=41 and level <=60:
    print(f"9000+{5*level}")

elif level >=61 and level <=80:
    print(f"9300+{2*level}")

elif level >=81 and level <=100:
    print(f"9500+{level}")

else :
    print("Tá errado boy")
    
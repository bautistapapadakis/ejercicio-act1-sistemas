texto = input("ingresa un texto:")
contador = 0

for letra in texto:
    if letra == "a":
        contador += 1

print("la cantidad de a", contador)
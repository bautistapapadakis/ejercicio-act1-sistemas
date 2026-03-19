
texto = input("Ingrese una palabra o frase: ")


print("Primera letra:", texto[0])


print("Última letra:", texto[-1])


posicion = int(input("Ingrese una posición: "))
if 0 <= posicion < len(texto):
    print("Letra en la posición", posicion, ":", texto[posicion])
else:
    print("Posición fuera de rango")


inicio = int(input("Ingrese posición inicial para la rebanada: "))
fin = int(input("Ingrese posición final para la rebanada: "))

print("Rebanada:", texto[inicio:fin])
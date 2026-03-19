suma = 0

while True:
    numero = int(input("Ingrese un número entero positivo (negativo para terminar): "))
    
    if numero < 0:
        break 
    
    suma += numero  

print("La suma total es:", suma)
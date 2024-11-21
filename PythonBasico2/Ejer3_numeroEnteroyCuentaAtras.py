numero = int(input("Introduce un número entero positivo: "))

for i in range(numero, -1, -1):
    
    print(i, end=', ' if i > 0 else '\n')
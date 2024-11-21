telefono = input("Introduce el número de teléfono (+34-numero-extension): ")

numero_extension = telefono.split('-')[1:-1]

print(f"El número de teléfono sin el prefijo y la extensión es: {'-'.join(numero_extension)}")
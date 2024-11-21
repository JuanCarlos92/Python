def calcular_total_factura(cantidad_sin_iva, iva=21):
    return cantidad_sin_iva * (1 + iva / 100)



cantidad = float(input("Introduce la cantidad sin IVA: "))
total = calcular_total_factura(cantidad)
print(f"El total de la factura es: {total}")
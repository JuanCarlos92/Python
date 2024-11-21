def obtener_calificaciones(notas):
    calificaciones = []
    
    for nota in notas:
        if nota >= 9:
            calificaciones.append("Sobresaliente")
        elif nota >= 7:
            calificaciones.append("Notable")
        elif nota >= 5:
            calificaciones.append("Aprobado")
        else:
            calificaciones.append("Suspenso")
    return calificaciones


notas = [int(x) for x in input("Introduce las notas separadas por espacio: ").split()]
print(obtener_calificaciones(notas))
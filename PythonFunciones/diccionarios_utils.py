def crearDiccionario(claves, valores):
    return dict(zip(claves, valores))

def revertirDiccionario(diccionario):
    return {v: k for k, v in diccionario.items()}
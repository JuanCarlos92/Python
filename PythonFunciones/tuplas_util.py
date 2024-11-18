def crearListaTuplas(lista):
    return [(index,value) for index, value in enumerate(lista)]

def contarElementosTupla(tupla, element):
    return tupla.count(element)
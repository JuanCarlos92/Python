from utilidades import ordenarLista
from filtrado import filtrarPares
from listas_util import eliminarDuplicados
from tuplas_util import  crearListaTuplas, contarElementosTupla
from diccionarios_utils import crearDiccionario, revertirDiccionario
from texto_utils import contarPalabras  

#Ejercicio 1: Ordenar lista
lista = [5, 3, 8, 1, 2]
listaOrdenada = ordenarLista(lista)
print(listaOrdenada)

#Ejercicio 2:  Filtrar Pares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filtrarPares(lista)
print(pares)

#Ejercicio 3: Eliminar duplicados
lista = [1, 2, 2, 3, 4, 4, 5]
nuevaLista = eliminarDuplicados(lista)
print(nuevaLista)

#Ejercicio 4: Desempaquetar tupla
def desempaquetarTupla(tupla):
    return tupla

tupla = (10, 20, 30)
a, b, c = desempaquetarTupla(tupla)
print(a, b, c) 

#Ejercicio 5 : Crear lista de tuplas
lista = ['a', 'b', 'c', 'd']
lista_tuplas = crearListaTuplas(lista)
print(lista_tuplas)

#Ejercicio 6: Contar elementos en tupla
tupla = (1, 2, 3, 1, 2, 1)
cuenta = contarElementosTupla(tupla, 1)
print(cuenta)

#Ejercicio 7: Crear diccionaro a partir de dos listas
claves = ['nombre', 'edad', 'ciudad']
valores = ['Carlos', 25, 'Madrid']
diccionario = crearDiccionario(claves, valores)
print(diccionario)

#Ejercicio 8: Contar ocurrencias de palabras
texto = "hola hola adios hola"
conteo = contarPalabras(texto)
print(conteo)

#Ejercicio 9: Revertir diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario_invertido = revertirDiccionario(diccionario)
print(diccionario_invertido)
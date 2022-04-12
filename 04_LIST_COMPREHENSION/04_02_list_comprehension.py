"""
lista = [ expresion(elemento) for elemento in objeto_iterable ]
"""

def calcular_cuadrado(numero):
    return numero**2


lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []
for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)

print("Ciclo for", lista_cuadrados)

lista_comprehension = [calcular_cuadrado(num) for num in lista_num]
print("List comprehension", lista_comprehension)

# Caso 1
total = sum([num for num in range(100)])
# Corección 
total = sum(num for num in range(100))


# Caso 2
[print(element) for element in range(1)]
# Corección 
for element in range(10):
    print(element)

# Caso 3
lista_anidada = [[1, 2], [3, 4], [5, 6]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)

# Corección 
lista_anidada = [[1, 2], [3, 4], [5, 6]]
valores_lista =[]
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)

print(valores_lista)

lista_num = [1, 2, 3, 4, 1, 2, 5, 6, 8]

set_pares = {num for num in lista_num if num % 2==0}
print(set_pares)

vocales = "aeiou"
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)
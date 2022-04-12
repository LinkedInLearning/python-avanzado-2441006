import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]
datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

archivo = open("datos.csv","w")
writer = csv.writer(archivo, delimiter=",")
archivo.close()


with open("datos.csv", "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)

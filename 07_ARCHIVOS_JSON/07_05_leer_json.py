import json

with open("persona.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

print(type(datos_json))
print(datos_json["nombre"])

import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "C:\\Users\\Ana\\Documents\\PythonAvanzado\\05_ARCHIVOS_CSV\\csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)

archivo_abierto = open(ruta_absoluta_os, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()

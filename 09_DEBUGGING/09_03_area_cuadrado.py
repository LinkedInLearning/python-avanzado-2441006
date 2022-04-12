def cacular_area_cuadrado(lado):
    """Calcula el área de un cuadrado al recibir la longitud del lado"""
    area = lado*lado
    return area


lado_cuadrados = [1, 3, 4]
area_cuadrados = []
for lado in lado_cuadrados:
    area = cacular_area_cuadrado(lado)
    area_cuadrados.append(area)

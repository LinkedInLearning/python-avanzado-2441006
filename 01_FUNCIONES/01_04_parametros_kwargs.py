def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])


funcion_kwargs(nombre="Paco", apellido="Botero")

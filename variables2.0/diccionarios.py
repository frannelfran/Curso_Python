# Crear diccionarios con dic
diccionario = dict(nombre="Juan", apellido="Pérez", edad=25)

# Las tuplas pueden ser claves
diccionario = {(1, 2): "Hola", (3, 4): "Adiós"}

# Crear un diccionario con fromleys
diccionario = dict.fromkeys(["nombre", "apellido"])
# diccionario = dict.fromkeys(["nombre", "apellido"], "desconocido") # Asigna un valor por defecto


print(diccionario)
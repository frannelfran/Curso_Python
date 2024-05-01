diccionario = {
  "nombre": "Carlos",
  "edad": 22,
  "curso": "Python"
}

claves = diccionario.keys() # Devuelve las claves del diccionario
# Obtener un elementocon con get
nombre = diccionario.get("nombre") # Devuelve el valor de la clave "nombre" -> También se puede hacer diccionario[0] como una lista (Te devuelve None si no encuentra el valor)
# Eliminar todo los elementos del diccionario
# diccionario.clear()

# Eliminar un elemento del diccionario
diccionario.pop("curso")
# diccionario.pop("nombre", "edad") # Eliminar más elementos

# Obtener un elemento iterable
elemento_iterable = diccionario.items()

print(claves)
print(nombre)
print(elemento_iterable)

diccionario = {
  "nombre": "Carlos",
  "apellido": "Gonzalez",
  "edad": 22
}

# Recorriendo un diccionario con su clave y valor
for key in diccionario.items():
  indice = key[0]
  valor = key[1]
  print(f"La clave es {indice} y el valor es {valor}")

# Almacena tuplas con cada clave y valor
for key in diccionario:
  print(key)
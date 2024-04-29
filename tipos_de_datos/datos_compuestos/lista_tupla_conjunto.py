# Lista (Se puede modificar)
lista = ["Franco", "Alla", True, 1.86]
print(lista) # ['Franco', 'Alla', True, 1.86]
lista[0] = "Juan" # Modificar un elemento de la lista

# Acceder a un elemento de la lista
print(lista[0]) # Franco (Elemento 0 de la lista)

# Tupla (No se puede modificar)
tupla = ("Franco", "Alla", True, 1.86)
# tupla[0] = "Juan" # Error
print(tupla) # ('Franco', 'Alla', True, 1.86)

# Conjunto (set) No se permiten datos repetidos como en c++
conjunto = {1, 2, 3, 4, 5}
# conjunto[0] = 3 # Error
conjunto = {1, 2, 3, 4, 5, 5, 6, 7, 8} # Se puede reconstruir el conjunto
# print(conjunto[0]) #Error
print(conjunto)

# Diccionario (dict) (clave: valor) Como un map en c++
diccionario = {
  "nombre" : "Franco",
  "apellido" : "Alla",
  "edad" : 22
}
print(diccionario) # {'nombre': 'Franco', 'apellido': 'Alla', 'edad': 22}
print(diccionario["nombre"]) # Franco (Acceder a un valor del diccionario)
print(diccionario["edad"] + 1) # 23 (Operaciones con valores del diccionario)
diccionario["nombre"] = "Juan" # Modificar un valor del diccionario
print(diccionario)
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [1, 2, 3, 4]

for animal in animales: # Iterar una lista
  print(animal)

# Recorriendo la lista números y múltiplicar esos números por 10
for numero in numeros:
  resultado = numero * 10
  print(resultado)

# Iterar ambas listas al mismo tiempo (Las listas deben tener el mismo número de elementos)
for numero, animal in zip(numeros, animales):
  print(numero, animal)

for num in range(5, 10): # Iterar un rango de números
  print(num)

# Recorrer una lista con su índice
for i in enumerate(numeros):
  # Lo primero es el índice y lo segundo es el valor
  indice = i[0]
  valor = i[1]
  print(f"El índice es {indice} y el valor es {valor}")

# Los else dentro de un bucle se ejecutan siempre y cuando el bucle haya terminado
for num in numeros:
  print(num)
else:
  print("El bucle ha terminado")

# Para las tuplas es lo mismo, esdecir, se itera de la misma forma
# Forma no óptima de sumar valores
def suma(lista):
  suma = 0
  for numero in lista:
    suma += numero
  return suma

resultado = suma([1, 2, 3, 4, 5])
print(resultado)

# Forma óptima de sumar valores
def suma(nombre, *numeros): # El asterísco convierte todos los argumentos en uno solo (Siempre tiene que ser el último parámetro)
  return f"Hola {nombre}, la suma de los números es: {sum(numeros)}"

resultado = suma("Lucas", 1, 2, 3, 4, 5)
print(resultado)
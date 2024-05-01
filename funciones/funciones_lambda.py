multiplicar_por_dos = lambda x : x * 2 # Con lambda se puede crear funciones anónimas -> Sirve para funciones pequeñas

numeros = [1, 2, 3, 4, 5]
# Función común que diga si un número es par o impar
def es_par(n):
  return n % 2 == 0

# Usando filter cómo función común
numeros_pares = filter(es_par, numeros) # Filter ejecuta la función para cada elemento de la lista
print(list(numeros_pares)) # Muestra la lista con los números pares

numeros_pares = filter(lambda numero : numero % 2 == 0, numeros) # Usando lambda
print(numeros_pares)
print(multiplicar_por_dos(2))
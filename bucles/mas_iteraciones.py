frutas = ["manzana", "pera", "uva", "sandía", "mango", "kiwi", "fresa", "naranja", "plátano", "cereza"]
texto = "Hola Mundo"
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for fruta in frutas:
  if (fruta == "kiwi"): # Si la fruta es kiwi, se salta a la siguiente iteración
    continue
  elif (fruta == "naranja"): # Si la fruta es naranja, se rompe el bucle
    break
  print(fruta)

# Recorrer una cadena de texto
for letra in texto:
  print(letra)

# for en una sola línea de código (duplicamos los números de una lista)
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
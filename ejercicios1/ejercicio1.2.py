frase = input("Decir una frase para calcular cuánto tiempo tardarías en decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
  print("¡Eso es mucho tiempo!")

print(f'Dijiste {cantidad_de_palabras} palabras,y tardarías {cantidad_de_palabras / 2} segundos en decirlo')
print(f'Dalto lo diría en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')
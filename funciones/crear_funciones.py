# Crear una función simple
def saludar():
  print("Hola, ¿cómo estás?")

# Ejecutar la función
saludar()

# Crear una función con un parámetro
def saludar(nombre, sexo):
  sexo = sexo.lower()
  if (sexo == "mujer"):
    adjetivo = "señora"
  elif(sexo == "hombre"):
    adjetivo = "señor"
  else:
    adjetivo = "amor"
  print(f"Hola {nombre} mi {adjetivo}, ¿cómo estás?")

# Ejecutar la función
saludar("Ana", "mujer")
saludar("Juan", "hombre")
saludar("Alex", "no binario")

# Crear una función que devuelva un valor
def crear_contraseña_random(num):
  chars = "abcdefghijklmn"
  num_entero = str(num) # Quedarse con el primer número
  num = int(num_entero[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
  return contraseña # Se pueden devolver varios valores separados por coma

password = crear_contraseña_random(98)
print(f"Tu contraseña es: {password}")
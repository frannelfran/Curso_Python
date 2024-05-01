# Función con 3 parámetros
def saludo(nombre, apellido, edad):
  return f"Hola {nombre} {apellido}, tienes {edad} años"

saludo_resultante = saludo("Lucas", "Gomez", 25)
saludo_resultante2 = saludo(nombre = "25", apellido = "Gomez", edad = "Lucas") # Se puede cambiar el orden de los argumentos
print(saludo_resultante)
print(saludo_resultante2)

# Función con 2 parámetros y un valor por defecto
def saludo(nombre, apellido, edad = 18): # Se puede asignar un valor por defecto a un parámetro
  return f"Hola {nombre} {apellido}, tienes {edad} años"

saludo_resultante = saludo("Lucas", "Gomez")
saludo_resultante2 = saludo("Lucas", "Gomez", edad = 25) # Se puede cambiar el valor por defecto

print(saludo_resultante)
print(saludo_resultante2)
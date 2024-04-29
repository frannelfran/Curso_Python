# Espacios de la memoria donde se almacenan los datos

# Variables
a = 3
b = 8
c = a + b
c += 1 # c = c + 1

nombre = "Juan"
nombre = "Pedro" # Las variables se pueden modificar
saludo = "Hola " + nombre + " ¿Cómo estas?"
fstring = f"Hola {nombre} ¿Cómo estas?" # Formateo de cadenas. Convertir un dato en texto
del nombre # Eliminar una variable

print(c) # 11
print(saludo) # Hola Pedro ¿ Cómo estas?
print(fstring) # Hola Pedro ¿ Cómo estas?
# Operadores de pertenenencia (in y not in)
print("ola" in saludo) # True # Verificar si una cadena de texto se encuentra en otra. También se le puede poner not in
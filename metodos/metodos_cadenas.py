cadena1 = "Hola soy Franco"
cadena2 = "Bienvenido a mi curso de Python"

resultado = dir(cadena1) # dir(dato) -> Muestra los métodos que se pueden aplicar a un dato
resultado = cadena1.upper() # Convertir todas las letras a mayúsculas
resultado = cadena1.lower() # Convertir todas las letras a minúsculasç
resultado = cadena1.capitalize() # Convertir la primera letra en mayúscula
print(resultado)

busqueda_find = cadena1.find("o") # Buscar la posición de la primera letra que coincida y si no la encuentra devuelve -1

# busqueda_index = cadena1.index("josif") # Buscar la posición de la primera letra que coincida pero devuelve una excepción si no la encuentra

es_numerico = cadena1.isnumeric() # Devuelve True si la cadena es numérica

es_alfanumerico = cadena1.isalpha() # Devuelve True si la cadena es alfanumérica

contar_coincidencias = cadena1.count("a") # Contar cuantas veces se repite una letra o cadena en la cadena

contar_caracteres = len(cadena1) # Contar cuantos caracteres tiene la cadena

empieza_con = cadena1.startswith("H") # Devuelve True si la cadena empieza con el caracter que se le pasa

remplazar = cadena1.replace("Franco", "Juan") # Remplaza una cadena por otra

cadena_separada = cadena1.split("o") # Separar cadenas con la cadena que le pasemos

print(es_numerico)
print(es_alfanumerico)
print(busqueda_find)
print(contar_coincidencias)
print(contar_caracteres)
print(empieza_con)
print(remplazar)
print(cadena_separada)
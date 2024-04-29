# Estructura: if condicion:
#               bloque de código
#           elif condicion:
#               bloque de código
#           else:
#               bloque de código

ingreso_mensual = 900
gasto = 20

if ingreso_mensual < 1000:
  print("Eres pobre")
  if gasto > 50:
    print("Deberías ahorrar más")
  else:
    print("Deberías ahorrar menos")

elif ingreso_mensual < 2000:
  print("Eres clase media")

else:
  print("Eres rico")
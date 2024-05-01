# Creando un set con set
conjunto = set(["dato1", "dato2", "dato3"])

# Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2", "dato3"])
conjunto2 = {conjunto1, "dato4", "dato5"}
print(conjunto)

# Teoría de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}
# Verificar que es un subconjunto
resultado = conjunto2.issubset(conjunto1) # Devuelve True si el conjunto2 es subconjunto de conjunto1
# Verificar que es un superconjunto
resultado2 = conjunto2.issuperset(conjunto1) # Devuelve True si el conjunto1 es superconjunto de conjunto2

# Verificar que sólo hay un número en común
resultado3 = conjunto2.isdisjoint(conjunto1) # Devuelve True si no hay elementos en común entre los conjuntos

print(resultado)
print(resultado2)
print(resultado3)
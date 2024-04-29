lista = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Crear una lista con list

contar_elementos = len(lista) # Contar cuantos elementos tiene la lista

lista.append(11) # Agregar un elemento al final de la lista
lista.insert(0, 0) # Agregar un elemento en la posición que le pasemos
lista.extend([12, 13, 14, 15]) # Agregar varios elementos al final de la lista (se agregan con corchetes)
lista.pop() # Eliminar el último elemento de la lista (Puede ir con o sin parámetros)
# lista.pop(0) # -1 PAra eliminar el ultimo elemento

lista.remove(10) # Eliminar un elemento de la lista
# lista.clear() # Eliminar todos los elementos de la lista

lista2 = [3, 20, 4, 1, 9, 7, 8, 6, 5, 2]
lista2.sort() # Ordenar la lista de menor a mayor (Si se utiliza el parametro reverse=True se ordena de mayor a menor) -> No funciona con listas que tengan elementos de diferentes tipos
lista2.sort(reverse=True) # Ordenar la lista de mayor a menor
lista.reverse() # Invertir la lista (No la ordena, solo la invierte, funciona para cualquier lista)

print(contar_elementos)
print(lista)
print(lista2)
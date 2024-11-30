#trabajando con listas
numeros = [1,2,3,4,5]
numeros.append(5)
print(numeros)

#usar listas como pilas

pila = []
pila.append(1)
pila.append(2)
print(pila.pop())#eliminar y devolver el ultimo lelemento

#usar listas como pilas
from collections import deque

cola = deque([1,2,3])
cola.append(4)
print(cola.popleft())#eliminar y devolver el primer elemento
print(cola)
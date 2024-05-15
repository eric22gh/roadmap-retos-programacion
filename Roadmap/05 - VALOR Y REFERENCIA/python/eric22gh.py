""" 
Valor y referencia

Asignación por valor: Se copia el valor y se crea una nueva referencia.
Asignación por referencia: Se copia la referencia al mismo objeto en memoria.
Pasada por valor: En tipos inmutables, pasar una variable a una función no afecta la variable original.
Pasada por referencia: En tipos mutables, pasar una variable a una función permite que los cambios dentro de la función afecten al objeto original.

Tipos inmutables: Números, cadenas de caracteres, tuplas, etc. No se pueden cambiar una vez creados.
Tipos mutables: Listas, diccionarios, conjuntos, etc. Se pueden cambiar después de su creación.

"""

# Ejemplo de asignación por valor (aparente) con tipos inmutables
a = 10
b = a  # b es una nueva referencia al valor 10
b += 5  # b ahora es 15, a sigue siendo 10
print(a)
print(a + b) 
eric = a + b 
print(eric)

print("Asignación por valor (aparente) con tipos inmutables:")
print(f"a = {a}")  # 10
print(f"b = {b}")  # 15

# Ejemplo de asignación por referencia (aparente) con tipos mutables
lista1 = [1, 2, 3]
lista3 = [10, 20, 35]
print(lista3)

lista2 = lista1  # lista2 es una referencia al mismo objeto que lista1
lista2.append(4)  # Esto modifica tanto lista1 como lista2
lista3.append(1) # añade un nnumero a la lista3
print(lista3)


print("\nAsignación por referencia (aparente) con tipos mutables:")
print(f"lista1 = {lista1}")  # [1, 2, 3, 4]
print(f"lista2 = {lista2}")  # [1, 2, 3, 4]

# Ejemplo de pasada por valor (aparente) con tipos inmutables
def incrementar(x):
    x += 1
    print(f"Valor dentro de la función: {x}")

y = 5
incrementar(y)
print(f"Valor fuera de la función: {y}")  # 5

# Ejemplo de pasada por referencia (aparente) con tipos mutables
def agregar_elemento(lista):
    lista.append(4)
    print(f"Lista dentro de la función: {lista}")

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print(f"Lista fuera de la función: {mi_lista}")  # [1, 2, 3, 4]

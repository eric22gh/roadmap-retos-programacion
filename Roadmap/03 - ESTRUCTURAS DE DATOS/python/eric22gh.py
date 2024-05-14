""" 
estructura de control de datos: sirven para organizar datos


"""

""" 
Las listas: colecciones ordenadas y mutables que permiten elementos duplicados.

"""

# Crear una lista vacía
lista = []

# Crear una lista con elementos
lista = [1, 2, 3, 4, 5]
lista2 = [22, 23, 25, 88]
list = ["eric", "thor", "mark"]
print(list)
list.append("edawrds") # lo añade al final

# Inserción
lista.append(6)       # Añadir un elemento al final
lista.insert(0, 0)    # Insertar en la posición 0 el valor 0

# Borrado
lista.remove(3)       # Eliminar el primer valor 3 encontrado
del lista[0]          # Eliminar el primer elemento (índice 0)
list.remove("thor")

# Actualización
lista[1] = 10         # Cambiar el valor del segundo elemento a 10

# Ordenación
lista.sort()          # Ordenar la lista de menor a mayor

# Listas
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(0, 0)
lista.remove(3)
del lista[0]
lista[1] = 10
lista.sort()
print("Lista:", lista)

""" 
Las tuplas; se pueden guardar mas de un dato, son colecciones ordenadas e inmutables que permiten elementos duplicados.
para usar en un programa q no se puedan cambiar los datos
"""

# Crear una tupla vacía
tupla = ()

# Crear una tupla con elementos
tupla = (1, 2, 3, 4, 5) # se puede con integer y strings
my: tuple = ("eric", "alex", "short", "36" )
print(tupla[2]) # imprimir la posicion de esa tupla
eric = sorted(my) # ordenar para luego imprimirlo
print(type(eric))

""" 
Los conjuntos son colecciones desordenadas de elementos únicos.
es buena para buscar datos y no se puede ordenar
"""

# Crear un conjunto vacío
conjunto = set()

# Crear un conjunto con elementos
conjunto = {1, 2, 3, 4, 5}


# Inserción
conjunto.add(6)       # Añadir un nuevo elemento

# Borrado
conjunto.remove(3)    # Eliminar un elemento específico

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.remove(3)
print("Conjunto:", conjunto)

set = {"rex", "alok", "gor"}
set.add ("wen")
print("set", set )

""" 
Los diccionarios son colecciones desordenadas de pares clave-valor.

"""

# Crear un diccionario vacío
diccionario = {}

# Crear un diccionario con elementos
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Diccionarios
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario['d'] = 4
del diccionario['b']
diccionario['a'] = 10
dict_ordenado_por_clave = dict(sorted(diccionario.items()))
dict_ordenado_por_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print("Diccionario ordenado por clave:", dict_ordenado_por_clave)
print("Diccionario ordenado por valor:", dict_ordenado_por_valor)

# Inserción
diccionario['d'] = 4       # Añadir un nuevo par clave-valor

# Borrado
# del diccionario['b']        # Eliminar un par clave-valor por su clave

# Actualización
diccionario['a'] = 10       # Cambiar el valor asociado a la clave 'a'

# Ordenación
# Los diccionarios en Python 3.7+ mantienen el orden de inserción, pero para ordenarlos por claves o valores:
# Ordenar por claves
dict_ordenado_por_clave = dict(sorted(diccionario.items()))

# Ordenar por valores
dict_ordenado_por_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))

""" 
Laboratorio: agenda

"""

def es_numero_telefono_valido(numero):
    """Verifica si el número de teléfono es válido."""
    # Retorna True si el número es completamente dígitos y su longitud es menor o igual a 11
    return numero.isdigit() and len(numero) <= 8

def insertar_contacto(agenda):
    """Inserta un nuevo contacto en la agenda."""
    # Solicita al usuario que introduzca el nombre del contacto
    nombre = input("Introduce el nombre del contacto: ")
    # Solicita al usuario que introduzca el número de teléfono del contacto
    numero = input("Introduce el número de teléfono: ")
    # Verifica si el número de teléfono es válido
    if es_numero_telefono_valido(numero):
        # Si es válido, añade el contacto a la agenda
        agenda[nombre] = numero
        print("Contacto añadido.")
    else:
        # Si no es válido, muestra un mensaje de error
        print("Número de teléfono no válido.")

def buscar_contacto(agenda):
    """Busca un contacto en la agenda."""
    # Solicita al usuario que introduzca el nombre del contacto a buscar
    nombre = input("Introduce el nombre del contacto a buscar: ")
    # Verifica si el contacto existe en la agenda
    if nombre in agenda:
        # Si existe, muestra el nombre y el número de teléfono del contacto
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        # Si no existe, muestra un mensaje de error
        print("Contacto no encontrado.")

def actualizar_contacto(agenda):
    """Actualiza un contacto existente en la agenda."""
    # Solicita al usuario que introduzca el nombre del contacto a actualizar
    nombre = input("Introduce el nombre del contacto a actualizar: ")
    # Verifica si el contacto existe en la agenda
    if nombre in agenda:
        # Solicita al usuario que introduzca el nuevo número de teléfono del contacto
        nuevo_numero = input("Introduce el nuevo número de teléfono: ")
        # Verifica si el nuevo número de teléfono es válido
        if es_numero_telefono_valido(nuevo_numero):
            # Si es válido, actualiza el número de teléfono del contacto
            agenda[nombre] = nuevo_numero
            print("Contacto actualizado.")
        else:
            # Si no es válido, muestra un mensaje de error
            print("Número de teléfono no válido.")
    else:
        # Si el contacto no existe, muestra un mensaje de error
        print("Contacto no encontrado.")

def eliminar_contacto(agenda):
    """Elimina un contacto de la agenda."""
    # Solicita al usuario que introduzca el nombre del contacto a eliminar
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    # Verifica si el contacto existe en la agenda
    if nombre in agenda:
        # Si existe, elimina el contacto de la agenda
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        # Si no existe, muestra un mensaje de error
        print("Contacto no encontrado.")

def main():
    # Crea un diccionario vacío para almacenar los contactos
    agenda = {}
    while True:
        # Muestra el menú de opciones
        print("\nAgenda de Contactos")
        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        # Solicita al usuario que seleccione una opción
        opcion = input("Selecciona una opción: ")
        
        # Ejecuta la función correspondiente a la opción seleccionada
        if opcion == "1":
            insertar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            # Si el usuario selecciona "5", sale del programa
            print("Saliendo del programa...")
            break
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

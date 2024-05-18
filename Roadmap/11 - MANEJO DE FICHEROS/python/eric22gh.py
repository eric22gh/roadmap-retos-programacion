""" 
Manejo de archivos: Desarrolla un programa capaz de crear 
un archivo que se llame como tu usuario

"""

import os # modulo que nos da operaciones para interactuar con sistema operativo

# Nombre del archivo
github_username = "eric22gh"
filename = f"{github_username}.txt"

# Contenido del archivo
nombre = "eric edwards"
edad = "30"
lenguaje_favorito = "Mi Lenguaje Favorito: Python"

# Crear y escribir en el archivo
with open(filename, 'w') as file:
    file.write(f"Nombre: {nombre}\n")
    file.write(f"Edad: {edad}\n")
    file.write(f"Lenguaje de programación favorito: {lenguaje_favorito}\n")

# Leer e imprimir el contenido del archivo
with open(filename, 'r') as file:
    contenido = file.read()
    print("Contenido del archivo:")
    print(contenido)

# Borrar el archivo
os.remove(filename)
print(f"El archivo {filename} ha sido borrado.")

""" 
Extra

Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.

 break se usa para salir de un programa
"""

import os # libreria que se usa para interactuar con el sistema de archivos.

filename = 'ventas.txt'

def mostrar_menu():
    print("\nMenú de Gestión de Ventas")
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir y borrar archivo")
    print("Seleccione una opción: ", end="")

def añadir_producto():
    nombre_producto = input("Nombre del producto: ")  # Pide el nombre del producto al usuario
    cantidad_vendida = int(input("Cantidad vendida: "))  # Pide la cantidad vendida
    precio = float(input("Precio: "))  # Pide el precio del producto

    with open(filename, 'a') as file:  # Abre el archivo en modo de añadir ('a')
        file.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")  # Escribe los datos en el archivo
    print(f"Producto {nombre_producto} añadido con éxito.")  # Confirma la adición del producto

def consultar_productos():
    if not os.path.exists(filename):  # Comprueba si el archivo existe
        print("No hay productos para mostrar.")  # Muestra un mensaje si el archivo no existe
        return
    
    with open(filename, 'r') as file:  # Abre el archivo en modo de lectura ('r')
        productos = file.readlines()  # Lee todas las líneas del archivo
        if not productos:  # Comprueba si el archivo está vacío
            print("No hay productos para mostrar.")  # Muestra un mensaje si está vacío
            return
        
        print("\nLista de productos:")  # Imprime el encabezado de la lista de productos
        for producto in productos:  # Itera sobre cada producto
            print(producto.strip())  # Imprime cada producto

def actualizar_producto():
    if not os.path.exists(filename):  # Comprueba si el archivo existe
        print("No hay productos para actualizar.")  # Muestra un mensaje si el archivo no existe
        return
    
    nombre_producto = input("Nombre del producto a actualizar: ")  # Pide el nombre del producto a actualizar
    productos_actualizados = []
    encontrado = False
    
    with open(filename, 'r') as file:  # Abre el archivo en modo de lectura
        productos = file.readlines()  # Lee todas las líneas del archivo
        for producto in productos:  # Itera sobre cada producto
            nombre, cantidad, precio = producto.strip().split(', ')  # Divide la línea en nombre, cantidad y precio
            if nombre == nombre_producto:  # Comprueba si el nombre coincide con el buscado
                cantidad = int(input("Nueva cantidad vendida: "))  # Pide la nueva cantidad vendida
                precio = float(input("Nuevo precio: "))  # Pide el nuevo precio
                productos_actualizados.append(f"{nombre}, {cantidad}, {precio}\n")  # Actualiza la lista de productos
                encontrado = True  # Marca que el producto ha sido encontrado
            else:
                productos_actualizados.append(producto)  # Mantiene el producto sin cambios
    
    if encontrado:
        with open(filename, 'w') as file:  # Abre el archivo en modo de escritura ('w')
            file.writelines(productos_actualizados)  # Escribe las líneas actualizadas en el archivo
        print(f"Producto {nombre_producto} actualizado con éxito.")  # Confirma la actualización
    else:
        print(f"Producto {nombre_producto} no encontrado.")  # Informa si el producto no se encontró

def eliminar_producto():
    if not os.path.exists(filename):  # Comprueba si el archivo existe
        print("No hay productos para eliminar.")  # Muestra un mensaje si el archivo no existe
        return
    
    nombre_producto = input("Nombre del producto a eliminar: ")  # Pide el nombre del producto a eliminar
    productos_actualizados = []
    encontrado = False
    
    with open(filename, 'r') as file:  # Abre el archivo en modo de lectura
        productos = file.readlines()  # Lee todas las líneas del archivo
        for producto in productos:  # Itera sobre cada producto
            nombre, cantidad, precio = producto.strip().split(', ')  # Divide la línea en nombre, cantidad y precio
            if nombre == nombre_producto:  # Comprueba si el nombre coincide con el buscado
                encontrado = True  # Marca que el producto ha sido encontrado
            else:
                productos_actualizados.append(producto)  # Mantiene el producto sin cambios
    
    if encontrado:
        with open(filename, 'w') as file:  # Abre el archivo en modo de escritura
            file.writelines(productos_actualizados)  # Escribe las líneas actualizadas en el archivo
        print(f"Producto {nombre_producto} eliminado con éxito.")  # Confirma la eliminación
    else:
        print(f"Producto {nombre_producto} no encontrado.")  # Informa si el producto no se encontró

def calcular_venta_total():
    if not os.path.exists(filename):  # Comprueba si el archivo existe
        print("No hay productos para calcular la venta total.")  # Muestra un mensaje si el archivo no existe
        return
    
    venta_total = 0
    
    with open(filename, 'r') as file:  # Abre el archivo en modo de lectura
        productos = file.readlines()  # Lee todas las líneas del archivo
        for producto in productos:  # Itera sobre cada producto
            nombre, cantidad, precio = producto.strip().split(', ')  # Divide la línea en nombre, cantidad y precio
            venta_total += int(cantidad) * float(precio)  # Calcula la venta total
    
    print(f"Venta total: {venta_total}")  # Imprime la venta total

def calcular_venta_por_producto():
    if not os.path.exists(filename):  # Comprueba si el archivo existe
        print("No hay productos para calcular la venta por producto.")  # Muestra un mensaje si el archivo no existe
        return
    
    ventas_por_producto = {}
    
    with open(filename, 'r') as file:  # Abre el archivo en modo de lectura
        productos = file.readlines()  # Lee todas las líneas del archivo
        for producto in productos:  # Itera sobre cada producto
            nombre, cantidad, precio = producto.strip().split(', ')  # Divide la línea en nombre, cantidad y precio
            if nombre in ventas_por_producto:
                ventas_por_producto[nombre] += int(cantidad) * float(precio)  # Suma la venta del producto existente
            else:
                ventas_por_producto[nombre] = int(cantidad) * float(precio)  # Añade un nuevo producto con su venta
    
    print("\nVentas por producto:")  # Imprime el encabezado de ventas por producto
    for nombre, venta in ventas_por_producto.items():  # Itera sobre cada producto y su venta
        print(f"{nombre}: {venta}")  # Imprime el nombre del producto y su venta

def salir_y_borrar_archivo():
    if os.path.exists(filename):  # Comprueba si el archivo existe
        os.remove(filename)  # Elimina el archivo
    print("Archivo borrado. Saliendo del programa.")  # Informa que el archivo ha sido borrado y el programa va a salir
    exit()  # Sale del programa

def main():
    while True:  # Bucle infinito para mantener el menú activo
        mostrar_menu()  # Muestra el menú
        opcion = input()  # Pide una opción al usuario
        if opcion == '1':
            añadir_producto()  # Llama a la función para añadir producto
        elif opcion == '2':
            consultar_productos()  # Llama a la función para consultar productos
        elif opcion == '3':
            actualizar_producto()  # Llama a la función para actualizar producto
        elif opcion == '4':
            eliminar_producto()  # Llama a la función para eliminar producto
        elif opcion == '5':
            calcular_venta_total()  # Llama a la función para calcular venta total
        elif opcion == '6':
            calcular_venta_por_producto()  # Llama a la función para calcular venta por producto
        elif opcion == '7':
            salir_y_borrar_archivo()  # Llama a la función para salir y borrar el archivo
        else:
            print("Opción no válida, por favor intente de nuevo.")  # Informa que la opción no es válida

if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa


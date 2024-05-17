""" 
RECURSIVIDAD
Cuando una función se llama a sí misma para resolver un problema

"""

# Llamamos a la función con el valor inicial de 5
def imprimir_descendente(n):
    # Imprimimos el número actual
    print(n)
    
    # Condición base: Si n es 1, no hacemos más llamadas recursivas
    if n == 1:
        return
    else:
        # Llamada recursiva con n-1
        imprimir_descendente(n - 1)

# Llamamos a la función con el valor inicial de 5
imprimir_descendente(5)

""" 
imprimir numeros del 100 al 0

"""
def imprimir_numeros(u):
    print(u)

    if u == 0:
        return
    else: 
        imprimir_numeros(u - 1)

imprimir_numeros(100)

""" def hello(): # bucle infinito
    hello()

hello() """

def num(g):
    if g == 1:
     print(g)
     num(g - 1)

num(20)



""" 
EXTRA 

"""

""" 
Calcular el Factorial de un Número, El factorial de un número 
𝑛 es el producto de todos los enteros positivos menores o iguales a n

"""
def factorial(n):
    # Si n es 0, el factorial es 1, si n no es igual a 0 se ejecuta else
    if n == 0:
        return 1
    else:
        # Llamada recursiva: n * factorial(n-1)
        return n * factorial(n - 1)

# Ejemplo: calcular el factorial de 5
print(factorial(5))  # llamar a la funcion factorial q tambien esta arriba
# Salida: 120

""" 
Calcular el Valor de un Elemento en la Sucesión de Fibonacci

"""

def fibonacci(n):
    # Condiciones base: Si n es 0 o 1, retornamos n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Llamada recursiva: fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo: calcular el elemento en la posición 7 de la sucesión de Fibonacci
print(fibonacci(7))  # Salida: 13

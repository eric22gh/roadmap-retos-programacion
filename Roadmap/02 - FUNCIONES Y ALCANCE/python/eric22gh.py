# funciones, son bloques de codigo reutilizables que ejecutan codigo

def saludar(nombre):
    print("Hola", nombre)
saludar("eric")

def suma(a, b): # ejecuta codigo dentro de este bloque 
    return a + b  
resultado = suma(3, 4)
print(resultado)

def resta(p, k):
    return p - k # bloque de codigo
digit = resta(200, 100)
print(digit)

def num(a):
    return a
horus = num(8)
print(horus)

def div (g, u):
    return g / u 
tor = div(20, 2)
print(tor)


# funciones con objetos
def obj():
    return"edwards"
names = obj
print(names())

def nombre():
    return ("eric")
saludar = nombre
print("hola", saludar())
#saludar("eric")

def return_greet():
    return "hola, hernandez"
print(return_greet())

def return_greet():
    return 8 + 8 
print(return_greet())

# retorno multiple
def multiple_return_greet(): 
    return 1, 2, 3, 4, 5, 6
print(multiple_return_greet())

def num_return_greet():
    return "hola", "edwards"
print(num_return_greet())

kor = num_return_greet
print(kor())

# varios argumentos
def var_greet(*names):
    for name in names: 
        print(F"Hola, {name}")

var_greet("Eric", "dolk", "horkat", "marcos")

# funcion dentro de otra funcion
def salida(): 
    def dentro():
        print("hola, estoy adentro")
    dentro() 
# salida llama a dentro y dentro llama a print ("hola, estoy dentro")
salida() 

""" funciones del lenguaje """

print(len("edawrds"))
print(type(True))
print("eric".upper())

""" 
extra 

"""

def imprimir_textos(texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
        contador += 1
    return contador

# Ejemplo de uso de la función
veces_impreso = imprimir_textos("hola mundo", "hola python")
# ejercicio tipico veces_impreso = imprimir_textos("Fizz", "Buzz")
print("Número de veces que se imprimió:", veces_impreso)

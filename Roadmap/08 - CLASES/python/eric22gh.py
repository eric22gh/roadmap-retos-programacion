""" 
CLASES: es un modelo que define un objeto, 
incluyendo sus atributos (datos) y métodos (funciones). 

"""

class Persona:
    def __init__(self, nombre, edad, ciudad):
        # Inicializador que define los atributos de la clase
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def imprimir_informacion(self):
        # Método que imprime los atributos de la clase
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30, "Madrid")

# Imprimir los atributos iniciales
persona1.imprimir_informacion()

# Modificar los atributos de la instancia
persona1.nombre = "Carlos"
persona1.edad = 35
persona1.ciudad = "Barcelona"

# Imprimir los atributos modificados
persona1.imprimir_informacion()

class user:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def print(self):
        print(f"nombre: {self.name} | edad: {self.age} | city: {self.city}")

my_user = user("alex", 52, "Lagos, Nigeria") 

my_user.print()
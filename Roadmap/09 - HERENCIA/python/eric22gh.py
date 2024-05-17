"""
Herencia: Concepto fundamental en la programación orientada a objetos, 
permite que una clase (subclase) herede atributos y métodos de otra clase (superclase).
Esto permite la reutilización de código y la creación de jerarquías de clases.

Polimorfismo:  permite que una misma interfaz o método se comporte 
de diferentes maneras en distintas clases. 
permite que una función tome diferentes formas
según el contexto en el que se utilice.

"""

# Definición de la superclase Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito por las subclases

# Definición de la subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Definición de la subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Crear instancias de Perro y Gato
mi_perro = Perro("Rex")
mi_gato = Gato("Mimi")

# Llamar al método hacer_sonido para cada instancia
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()

######### clases ######
""" 

class animals: 

    def __init__(self, name: str):
        self.name = name 

    def sound():
        pass

class frog(animals): 

    def __init__(self, name: str):
        self.name = name 

    def sound():
        print("este animal hace el sonido del sapo")
class fish(animals): 

    def __init__(self, name: str):
        self.name = name 

    def sound():
        print("este animal hace el sonido del pez")

#herencia nos sirve para heredar funciones o metodos

# subclases: que el sapo herede el comportamiento del lizart osea 
# print("este animal hace el sonido del lagarto")
class frog(animals): 
    def sound(self, name: str):
        print("este animal hace el sonido del largarto")

my_animal = animals("tito")
my_animal.sound() 

 """

####################

class employee: 

    def __init__(self, id: int, name: str, lastname: str):
        self.id = id 
        self.name = name
        self.lastname = lastname
        self.employee = [] # lista vacia
    def add(self, employee):
        self.employee.append(employee)


# todos van a tener un id, un nombre y un apellido
# todos los sigueintes heredan caracteristicas de employee

class BOSS(employee): 
    def coordinate(self):
        print(F"{self.name} esta coordinando el proyecto")

class Developer(employee): 
      def __init__(self, id: int, name: str):
        super().__init__(id, name)

class testing(employee):
     def test(self):
        print(F"{self.name} esta testeando el codigo")


# Crear instancias de empleados
emp1 = employee(1, "John", "Doe")
emp2 = employee(2, "Jane", "Smith")

# Añadir emp2 a la lista de empleados de emp1
#emp1.add(emp2)

# Verificar que emp2 ha sido añadido a la lista de emp1
print(employee)

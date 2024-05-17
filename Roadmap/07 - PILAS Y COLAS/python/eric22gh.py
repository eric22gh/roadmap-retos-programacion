""" 
PILAS(pilas o lifo) Y COLAS
Una pila es una estructura de datos que sigue el principio 
LIFO (Last In, First Out), lo que significa que el último 
elemento en ser añadido es el primero en ser removido.


Operaciones principales:
push: Añadir un elemento al tope de la pila.
pop: Remover y devolver el elemento del tope de la pila.
peek: Devolver el elemento del tope de la pila sin removerlo.
is_empty: Verificar si la pila está vacía.

"""
stock = []
stock.append("20")
stock.append("30")
stock.append("40")
stock.append("50")

print(stock)

class Stack:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía para almacenar los elementos

    def push(self, item):
        # Añadimos un elemento al tope de la pila
        self.items.append(item)
        print(f"Elemento {item} añadido a la pila.")

    def pop(self):
        # Removemos y devolvemos el elemento del tope de la pila
        if not self.is_empty():
            return self.items.pop()
        else:
            return "La pila está vacía."

    def peek(self):
        # Devolvemos el elemento del tope de la pila sin removerlo
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía."

    def is_empty(self):
        # Verificamos si la pila está vacía
        return len(self.items) == 0

# Ejemplo de uso
pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
print(f"Elemento en el tope de la pila: {pila.peek()}")
print(f"Elemento removido: {pila.pop()}")
print(f"Elemento en el tope de la pila: {pila.peek()}")

""" 
Cola (Queue) es una estructura de datos que sigue el 
principio FIFO (First In, First Out), 
lo que significa que el primer elemento en ser añadido
es el primero en ser removido.


Operaciones principales:
enqueue: Añadir un elemento al final de la cola.
dequeue: Remover y devolver el primer elemento de la cola.
front: Devolver el primer elemento de la cola sin removerlo.
is_empty: Verificar si la cola está vacía.
"""

class Queue:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía para almacenar los elementos

    def enqueue(self, item):
        # Añadimos un elemento al final de la cola
        self.items.append(item)
        print(f"Elemento {item} añadido a la cola.")

    def dequeue(self):
        # Removemos y devolvemos el primer elemento de la cola
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "La cola está vacía."

    def front(self):
        # Devolvemos el primer elemento de la cola sin removerlo
        if not self.is_empty():
            return self.items[0]
        else:
            return "La cola está vacía."

    def is_empty(self):
        # Verificamos si la cola está vacía
        return len(self.items) == 0

# Ejemplo de uso
cola = Queue()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
print(f"Primer elemento de la cola: {cola.front()}")
print(f"Elemento removido: {cola.dequeue()}")
print(f"Primer elemento de la cola: {cola.front()}")

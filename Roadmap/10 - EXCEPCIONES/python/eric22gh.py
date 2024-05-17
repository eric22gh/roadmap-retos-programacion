""" 
EXCEPTIONES: try, except. permite que un programa 
controle errores y los maneje de manera adecuada, 
evitando que el programa se detenga de manera inesperada.

"""

# Provocar un error al intentar dividir por cero
try:
    resultado = 10 / 0  # codigo que provocará el error
except ZeroDivisionError as error:
    print("¡Error de división por cero!")
    print("Error:", error)
    # Aquí puedes agregar código para manejar la excepción, si es necesario

# Provocar un error al intentar acceder a un índice no existente en una lista
try:
    lista = [1, 2, 3]
    elemento = lista[4]  # Esto provocará una excepción IndexError
except IndexError as error:
    print("¡Error de índice fuera de rango!")
    print("Error:", error)
    # Aquí puedes agregar código para manejar la excepción, si es necesario

print("El programa continúa después de manejar las excepciones.")

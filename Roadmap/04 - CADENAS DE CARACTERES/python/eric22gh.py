""" 
Cadenas de caracteres

"""

# Cadena de ejemplo
cadena = "Hola, Mundo!"

# 1. Acceso a caracteres específicos o indexacion
# Puedes acceder a un carácter específico de una cadena usando índices.
print(cadena[0])  # H -> Accede al primer carácter
print(cadena[-1]) # ! -> Accede al último carácter

# 2. Subcadenas 
# Puedes extraer una porción de la cadena usando slicing.
print(cadena[0:4])  # Hola -> Subcadena desde el índice 0 hasta el 4 (sin incluirlo)
print(cadena[5:])   # , Mundo! -> Subcadena desde el índice 5 hasta el final
print(cadena[:5])   # Hola, -> Subcadena desde el inicio hasta el índice 5 (sin incluirlo)
print(cadena[-6:])  # Mundo! -> Subcadena desde el sexto carácter desde el final hasta el final

# 3. Longitud
# Puedes obtener la longitud (número de caracteres) de una cadena usando len().
print(len(cadena))  # 12 -> Longitud de la cadena "Hola, Mundo!"

# 4. Concatenación
# Puedes unir dos o más cadenas usando el operador +.
saludo = "Hola"
nombre = "Mundo"
frase = saludo + ", " + nombre + "!"
print(frase)  # Hola, Mundo! -> Concatenación de varias cadenas

# 5. Repetición
# Puedes repetir una cadena un número específico de veces usando el operador *.
eco = "Echo! " * 3
print(eco)  # Echo! Echo! Echo! -> La cadena se repite tres veces

# 6. Recorrido
# Puedes recorrer cada carácter de una cadena usando un bucle for.
for caracter in cadena:
    print(caracter)  # Imprime cada carácter en una nueva línea

# 7. Conversión a mayúsculas y minúsculas
# Puedes convertir una cadena a mayúsculas usando upper() y a minúsculas usando lower().
print(cadena.upper())  # HOLA, MUNDO! -> Conversión a mayúsculas
print(cadena.lower())  # hola, mundo! -> Conversión a minúsculas

# 8. Reemplazo
# Puedes reemplazar todas las ocurrencias de una subcadena por otra usando replace().
print(cadena.replace("Mundo", "Amigo"))  # Hola, Amigo! -> Reemplaza "Mundo" por "Amigo"

# 9. División
# Puedes dividir una cadena en una lista de subcadenas usando split(). Por defecto, divide por espacios.
lista_palabras = cadena.split()
print(lista_palabras)  # ['Hola,', 'Mundo!'] -> Divide la cadena en palabras

# 10. Unión
# Puedes unir una lista de cadenas en una sola cadena usando join(), especificando un separador.
lista = ['Hola', 'Mundo']
unida = " ".join(lista)
print(unida)  # Hola Mundo -> Une la lista de palabras con un espacio como separador

# 11. Interpolación
# Puedes insertar valores en una cadena usando f-strings, format() o el operador %.
nombre = "Mundo"
print(f"Hola, {nombre}!")        # Hola, Mundo! -> Interpolación usando f-string
print("Hola, {}!".format(nombre)) # Hola, Mundo! -> Interpolación usando format
print("Hola, %s!" % nombre)       # Hola, Mundo! -> Interpolación usando %

# 12. Verificación
# Puedes verificar si una cadena contiene otra cadena usando in o métodos como startswith() y endswith().
print("Mundo" in cadena)          # True -> Verifica si "Mundo" está en la cadena
print(cadena.startswith("Hola"))  # True -> Verifica si la cadena comienza con "Hola"
print(cadena.endswith("!"))       # True -> Verifica si la cadena termina con "!"

# 13. Eliminación de espacios en blanco
# Puedes eliminar espacios en blanco al inicio y al final de una cadena usando strip(), lstrip() y rstrip().
cadena_espacios = "  Hola, Mundo!  "
print(cadena_espacios.strip())   # "Hola, Mundo!" -> Elimina espacios al inicio y al final
print(cadena_espacios.lstrip())  # "Hola, Mundo!  " -> Elimina espacios al inicio
print(cadena_espacios.rstrip())  # "  Hola, Mundo!" -> Elimina espacios al final

# 14. Encontrar subcadenas
# Puedes encontrar la posición de la primera aparición de una subcadena usando find() o index().
print(cadena.find("Mundo"))   # 6 -> Encuentra la posición de "Mundo"
print(cadena.index("Mundo"))  # 6 -> Encuentra la posición de "Mundo"
print("a" in cadena)
print("o" in cadena)


# 15. Conteo de subcadenas
# Puedes contar cuántas veces aparece una subcadena en una cadena usando count().
print(cadena.count("o"))  # 2 -> Cuenta el número de veces que aparece "o"

# 16. Capitalización
# Puedes capitalizar la primera letra de la cadena usando capitalize().
print(cadena.capitalize())  # Hola, mundo! -> Capitaliza la primera letra
print(cadena.title())  


# 17. Inversión de una cadena
# Puedes invertir una cadena usando slicing con un paso negativo.
print(cadena[::-1])  # !odnuM ,aloH -> Invierte la cadena

# 18. transformaciones numericas
eric = "122566" # solo con print(eric) tira en cosola strings, se convierten con el eric = int(eric)
eric = int(eric)
print(eric)

eri = "122566.25"
eri = float(eri)
print(eri)

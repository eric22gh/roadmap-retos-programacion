# operadores de comparacion
8 > 1 # mayor que 
5 < 100 # menor que
8 == 8 # igual a
5 >= 4 # mayor igual
6 <= 5  # menor igual

# operadores aritmeticos
10 % 100 # modulo, el 10 porciento de 100 es # 
100 ** 3 # elevado
100 - 20 # resta
100 + 20 # suma 
22 / 2 # division
22 * 2 # multiplicacion
5 != 100 # distinto de 

# operadores logicos
5 > 2 and 100 == 100 # and, &&: dos cosas tiene que ser ciertas
100 == 5 or 4 > 500 # or, ||: que se cumpla una condicion


# ejemplos 
print(5+5)
print(556-5)
print(100/5)
print(25*5)
print(55>5)
print(10%100)
print(f"Modulo: 20 % 1000 es = {20 % 100}") # pone entre corchetes para que se pueda aplicar la operacion


# condicionales
my_str = "eric"

if my_str == "eric":
    print(" bienvenido a casa eric")
else:
    print(" eric no esta en casa")

###################################

my_st = "edwards"

if my_st == "eric":
    print(" bienvenido a casa eric")
elif my_st == "edwards":
    print("sali de vacaciones")
else:
    print("eric no esta en casa")

# for recorre los elememntos de una lista uno x uno
for i in range(22):
    print(i)

# bucle infinitp while
i = 2
while i <= 10:
    print(i) # hasta aqui continuaria imprimiendo el valor de i
    i += 1 # cada vez que pasa el bucle le va sumando 1 al valor i


# imprimir los numeros entre el 10 y 55, pares y que no sean ni el 16 ni multiplos de 3
# recorre la lista num del 10 al 55
for num in range(10,56): 
    # # revisa si en esa lista hay numeros par
    if num % 2==0 and num != 16 and num % 3 != 0:
        # si todas las codiciones anteriores en la lista son ciertas print num(el valor de la lista sin los numeros pares)
        print(num)



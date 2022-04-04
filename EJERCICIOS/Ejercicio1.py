# Escribí un programa que solicite al usuario que ingrese su nombre.
# El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar
# en pantalla el texto “Ahora estás en la matrix, [usuario]”,
# donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado

nombre = input("Cuál es tu nombre? ")
print(f"Ahora estás en la matrix, {nombre}")

# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo
# en una variable. A continuación, el programa debe solicitar al usuario que ingrese un
# número entero y guardarlo en otra variable. En una tercera variable se deberá guardar
# el resultado de la suma de los dos números ingresados por el usuario.
# Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”,
# donde “[suma]” se reemplazará por el resultado de la operación

numero1 = float(input("Escribe un numero decimal: "))
numero2 = int(input("Escribe un numero entero: "))
resultado = numero1 + numero2
print(f"El resultado de la suma es {resultado}")

# Escribí un programa que solicite al usuario dos números y los almacene en dos variables.
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado
# en pantalla. A continuación, el programa debe solicitar al usuario que ingrese un tercer número,
# el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado
# de la multiplicación de este nuevo número por el resultado de la suma anterior.

n1 = int(input("Escribe num 1: "))
n2 = int(input("Escribe num 2: "))
suma = n1 + n2
print(f"La suma es: {suma}")
n3 = int(input("Escribe un nuevo numero"))
multip = int(n3 * suma)
print(f"La multiplicacion de la suma por el ultimo numero es: {multip}")




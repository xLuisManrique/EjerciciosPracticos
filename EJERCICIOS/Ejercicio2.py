# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros
# recorridos por una motocicleta y la cantidad de litros de combustible que
# consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

kilometros = float(input("Cuántos kilometros recorristes: "))
combustilbe = float(input("Cuántos galones de combustibles gastaste: "))
consumo = round(kilometros/combustilbe)
print(f"El consumo por kilometro es de {consumo}\n")


# Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit
# (debe permitir decimales) y le muestre el equivalente en grados Celsius.
# La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)

temperatura = float(input("Ingrese una temperatura: "))
celsius = ((5/9) * (temperatura-32))
temperatura_final = round(celsius, 2)
print(f"Su temperatura en Farenheit son {temperatura}\nque equivalen a"
      f"{temperatura_final} grados celsius\n")


# Escribe un programa que solicite al usuario ingresar tres números para
# luego mostrarleel promedio de los tres

nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Segunda nota: "))
print(f"Su promedio de notas es de: {(nota1+nota2+nota3)/3}\n")


# Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando
# todo en una única variable. A continuación, mostrar el resultado final en pantalla.

numero = int(input("Digita un numero: "))
print(f"Descontado el 15% queda: {numero-(numero*15)/100}\n")

# Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se
# guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación
# de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla

palabra = (input("Dime una palabra: ")) + " " + (input("Dime otra palabra: "))
print(palabra)

# Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una
# variable. A continuación, mostrar en pantalla la primera letra del texto ingresado.
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que
# tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número
# entre 0 y 4) y almacenar este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice

texto = input("Ingresa un texto cualquiera:\n")
print("La primera Letra del texto es:", texto[0])
print("Ingresa un numero positivo menor a: ", len(texto))
numero_ingresado = int(input())
print("La letra que esta en la posiciones: ", texto[numero_ingresado])


# Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en
# el último año y almacene ese número en una variable. A continuación mostrar en
# pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

show = int(input("Cuantos shows has visto en el ultimo año"))
print(show>3)




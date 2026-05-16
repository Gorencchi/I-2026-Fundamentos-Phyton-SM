import math
print("Hola, bienvenido a la calculadora de imc")
#definimos variables
nombre = input("Cuál es tu nombre? ")
apellidos = input("Cuales son tus apellidos? ")
edad = int(input("Escribe tu edad "))
peso = int(input("Escribe tu peso en kg "))
altura = float(input("Escribe tu altura en metros "))
print("Calculando imc...")
#calcular el imc
imc = peso/altura**2
if imc >= 30:
    print(nombre, apellidos, "tu imc es", imc, "y estás en la categoría de obesidad")
elif 25 <= imc <= 29.9:
    print(nombre, apellidos, "tu imc es", imc, "y estás en la categoría de sobrepeso")
elif imc >= 18.5:
    print(nombre, apellidos, "tu imc es", imc, "y estás en la categoría de peso normal")
else:
    print(nombre, apellidos, "tu imc es", imc, "y estás en la categoría de bajo peso")   
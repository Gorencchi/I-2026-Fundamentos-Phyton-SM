print("Hola mundo")
##Acá se configuran los valores a las variables.
nombre = "Samu"
edad:int = int(input("Cual es tu edad? "))
altura = 1.53
##Acá se calcula el año de nacimiento.
anno_de_nacimiento = 2026 - edad
print ("Mi año de nacimiento es", anno_de_nacimiento)
##Acá se calcula si el usuario es mayor o menor de edad.
if edad >= 18:
 print ("Eres mayor de edad")
else:
    print("eres menor de edad")
##Acá se verifica si el usuario es o si no es, o si quizá es. Si es true es porque el usuario si es real, si es false es porque el usuario no es real, y si es quizá es porque el usuario cumple una de las dos condiciones.
    no_soy_yo = not(nombre == "Samu" and edad == 17)
    print(no_soy_yo)
    soy_yo = nombre == "Samu" and edad == 17
    print(soy_yo)
    quizas_soy_yo = nombre == "Samu" or edad == 17
    print(quizas_soy_yo)
    x = 10
    x += 5
    print (x)
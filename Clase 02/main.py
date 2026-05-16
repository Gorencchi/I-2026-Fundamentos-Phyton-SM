print("Hola mundo")
nombre = "Samu"
edad:int = int(input("Cual es tu edad? "))
altura = 1.53
anno_de_nacimiento = 2026 - edad
print ("Mi año de nacimiento es", anno_de_nacimiento)
if edad >= 18:
 print ("Eres mayor de edad")
else:
    print("eres menor de edad")
no_soy_yo = not(nombre == "Samu" and edad == 17)
print(no_soy_yo)
soy_yo = nombre == "Samu" and edad == 17
print(soy_yo)
quizas_soy_yo = nombre == "Samu" or edad == 17
print(quizas_soy_yo)
x = 10
x += 5
print (x)

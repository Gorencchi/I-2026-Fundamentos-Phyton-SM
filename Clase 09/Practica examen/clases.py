class Mascotas():
    def __init__(self, edad, nombre, especie):
        self.edad = edad
        self.nombre = nombre
        self.especie = especie
        
    def mostrar_informacion_general():
        print ("Nombre de la mascota: {self.nombre}/n, edad de la mascota: {self.edad}/n, especie: {self.especie}/n")
        
#Programa principal
mascotas = []
print("=============Registro de mascotas=============")
while True:
    print("Menú de opciones")
    print("1. Registrar mascotas")
    print("2. Mostrar todas las mascotas")
    print("3. Salir")
    seleccion = (str(input("Escriba una opción a elegir: ")))
    if seleccion == 1:
        cantidad = input("Escriba la cantidad de mascotas a registrar: ")
        for i in range(cantidad):
            print("Mascotas que se iran a registrar: ", {Mascotas + 1})
            edad = (str(input("Escriba la edad de la mascota: ")))
            nombre = input("Escriba el nombre de la mascota: ")
            especie = input("Escriba el nombre de la especie: ")
            mascota = Mascotas(nombre,edad,especie)
            mascotas.append(Mascotas)
            print("Registro guardado con exito")
    if seleccion == 2:
        for i in range(len(mascotas)):
            print("Mascota registrada: ", {Mascotas + 1})
            Mascotas[1].mostrar_informacion_general
    elif seleccion == 3:
        print("Saliendo del programa")
        break

class Vehiculo():
    def __init__(self, placa, año, marca, modelo):
        self.placa = placa
        self.año = año
        self.marca = marca
        self.modelo = modelo
    def mostrar(self):
        print(f"Placa: {self.placa}\n Año: {self.año}\n Marca: {self.marca}\n Modelo: {self.modelo}")

#programa principal :b
cantidad = 0
opcion = 0
vehiculo = []
while True:
    print("==================================")
    print("Bienvenido al registro de autos")
    print("==================================")
    print("Menú de opciones")
    print("1. Registrar autos")
    print("2. Mostrar autos registrados")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        cantidad = int(input("Escriba la cantidad de autos a registrar: "))
        for i in range(cantidad):
            print(f"Auto a registrar: {i + 1}")
            placa = input("Escriba la placa: ")
            año = int(input("Escriba el año: "))
            marca = input("Escriba la marca: ")
            modelo = input("Escriba el modelo: ")
            auto = Vehiculo(placa, año, marca, modelo)
            vehiculo.append(auto)
            print("Auto(s) registrados con exito..")
            print("Volviendo al menú")
    elif opcion == 2:
        print("Mostrando autos registrados en el sistema...")
        for i in range(len(vehiculo)):
            print(f"Auto(s) registrado(s): {i + 1}")
            auto.mostrar()
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opcion no valida, seleccione una opcion en el menú")
        
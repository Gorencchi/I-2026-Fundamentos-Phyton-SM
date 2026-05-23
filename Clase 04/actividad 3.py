print("Bienvenido al cajero automatico")
print("Cargando menú de opciones...")
print("Ingrese su numero de cuenta: ")
cuenta = input()
while True:
    print("Menu de opciones")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    select = int(input("Elige una opcion: "))
    if select == 1:
        saldo = 0
        print("Tu dinero disponible en tu cuenta es de", saldo, "colones")
    elif select == 2:
        deposito = int(input("Cuanto dinero quieres depositar? "))
        saldo += deposito
        print(f"Tu dinero disponible en tu cuenta es de {saldo} colones")
    elif select == 3:
        retiro = int(input("Cuanto dinero quieres retirar? "))
        if retiro > saldo:
            print ("No tienes el dinero suficiente para retirar :(")
        else:
            saldo -= retiro
            print(f"Retiro completado.")
    elif select == 4:
        print("Gracias por usar el cajero automatico, vuelva pronto :)")
        break
    else:       print("Opcion no valida, por favor elige una opcion del menu")
    
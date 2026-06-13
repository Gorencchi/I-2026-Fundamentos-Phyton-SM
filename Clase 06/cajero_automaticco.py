#Variables
saldo = 0
deposito = 0
retirar = 0

#Definicion de funciones
def retirarsaldo():
    global saldo
    retiro = int(input("Cuanto dinero quieres retirar? "))
    if retiro > saldo:
        print ("No tienes el dinero suficiente para retirar :(")
    else:
        saldo -= retiro
        print(f"Su saldo restante es de {saldo}")
        print(f"Retiro completado.")
        
def consultarsaldo():
    global saldo
    print("Tu dinero disponible en tu cuenta es de", saldo, "colones")

def depositar():
    global saldo
    deposito = int(input("Cuanto dinero quieres depositar? "))
    saldo+= deposito
    print(f"Tu dinero disponible en tu cuenta es de {saldo} colones")

#Programa principal
print("Bienvenido al cajero automatico")
print("Cargando menú de opciones...")
while True:
    print("Menu de opciones")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    select = int(input("Elige una opcion: "))
    if select == 1:  
        consultarsaldo()
    elif select == 2:
       depositar()
    elif select == 3:
       retirarsaldo()  
    elif select == 4:
        print("Gracias por usar el cajero automatico, vuelva pronto :)")
        break
    else:       print("Opcion no valida, por favor elige una opcion del menu")
print("Registro de estudiantes")
while True:
    print("Menu de opciones")
    print("1. Registrar estudiante")
    print("2. Estudiantes registrados")
    print("3. Salir")
    archivo = open("C:\\Users\\Personas Invitadas\\Desktop\\I-2026-Fundamentos-Phyton-SM\\Clase 06\\estudiantes.txt", "a")
    seleccion = int(input("Seleccione una opcion: "))
    if seleccion == 1:
        nombre = input("Escriba el nombre del estudiante: ")
        cedula = int(input("Escriba la cedula del estudiante: "))
        nota = float(input("Escriba la nota del estudiante: "))
        if nota > 100:
            print("La nota no es valida, tiene que ser un valor menor a 100")
        else:
            archivo.write(f"Nombre:{nombre} | N. cedula: {cedula} | Nota: {nota}\n")
            print("Estudiante registrado con exito")
        archivo.close()
    if seleccion == 2:
        archivo = open("C:\\Users\\Personas Invitadas\\Desktop\\I-2026-Fundamentos-Phyton-SM\\Clase 06\\estudiantes.txt", "r")
        print(f"\tEstudiantes registrados:\n\t{archivo.read()}")
        archivo.close()
    if seleccion == 3:
        break
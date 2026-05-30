nombre = input("Escriba su nombre: ")
print("Hola",nombre, "bienvenido al control de inventario")
while True:
    print("1. Registro de productos")
    print("2. Calcular valor total de un producto")
    print("3. Valor general del inventario")
    print("4. Salir")
    select = int(input("Seleccione una opción: "))
    precio = 0
    producto = 0
    cantidad = 0
    producto2 = 0
    precio2 = 0
    cantidad2 = 0
    producto_calcular = 0
    valor_inventario = 0
    if select == 1:
        producto = input("Escriba el nombre del producto: ")
        precio = int(input("Escribe el precio del producto: "))
        cantidad = int(input("Escriba la cantidad disponible: "))
        if cantidad and precio == 0:
            print("Escriba un valor mayor a 0 en precio y cantidad")
        else:
            print ("El producto", producto,"tiene un precio de", precio,"y su cantidad en el inventario es de", cantidad)
        otro_producto = input("Desea registrar otro producto? 1. si 2. no")
        if otro_producto == "1":
            producto2 = input("Escriba el nombre del producto: ")
            precio2 = int(input("Escribe el precio del producto: "))
            cantidad2 = int(input("Escriba la cantidad disponible: "))
            if cantidad2 and precio2 == 0:
                print("Escriba un valor mayor a 0 en precio y cantidad")
            else:
                print ("El producto", producto2,"tiene un precio de", precio2,"y su cantidad en el inventario es de", cantidad2)
                print("Productos registrados: ", producto, "y", producto2)
        else:
            print("Producto registrado: ", producto)
    if select == 2: 
        print("Bienvenido a la calculadora de valor total")
        if  producto == 0 and precio == 0 and cantidad == 0 and producto2 == 0 and precio2 == 0 and cantidad2 == 0:
                print("No hay productos registrados, por favor registre un producto para usar esta función")
        else:
            print("Productos registrados: ", producto, "y", producto2)
        producto_calcular = input("Escriba el nombre del producto a calcular: ")
        if producto_calcular == producto: 
                cantidad_calcular = int(input("Escriba la cantidad de productos: "))         
                valor_total = precio * cantidad_calcular
                print("El valor total de", cantidad_calcular, "productos", producto, "es de:", valor_total)
        elif producto_calcular == producto2:
                cantidad_calcular2 = int(input("Escriba la cantidad de productos: "))
                valor_total2 = precio2 * cantidad_calcular2
                print("El valor total de", cantidad_calcular2, "productos", producto2, "es de:", valor_total2)
        else:
            print("No hay productos registrados, por favor registre un producto para usar esta función")
    if select == 3:
        print   ("Bienvenido a la calculadora de valor general del inventario")
        if  producto == 0 and precio == 0 and cantidad == 0:
                print("No hay productos registrados, por favor registre un producto para usar esta función")
        else:
             print(producto, precio, cantidad)
             print(producto2, precio2, cantidad2)
             valor_inventario = (precio * cantidad) + (precio2 * cantidad2)
             print("El valor total del inventario es de:", valor_inventario)     
    if select == 4:
        print("Gracias por usar el control de inventario, hasta luego", nombre)
        break   
    else:
        print("Opción no válida, por favor seleccione una opción del 1 al 4")
class Seleccion:
    def __init__(self, pais, confederacion):#init es el constructor
        self.jugadores = []
        self.pais = pais
        self.confederacion = confederacion
    def agregar(self, jugador):
        if jugador and jugador not in self.jugadores:
            self.jugadores.append(jugador)  # agrega jugadores a la lista si no existen
            return True
        return False

    def eliminar(self, jugador):
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)
            return True
        return False

pais = input("Ingrese el nombre del país: ")
confederacion = input("Escriba la confederacion: ")
jugador = input("Escriba el nombre del jugador: ")
argentina = Seleccion("Argentina", "CONMEBOL")
brasil = Seleccion("Brasil", "CONMEBOL")
espanna = Seleccion("España", "CONMEBOL")
seleccion = Seleccion(pais, confederacion)

argentina.agregar("Lionel Messi")
argentina.agregar("Angel Di Maria")
brasil.agregar("Neymar")
seleccion.agregar(jugador)
espanna.agregar("Lamine Yamal")
espanna.agregar("Gabi")
print(argentina.jugadores)
print(brasil.jugadores)
print (espanna.jugadores)
argentina.eliminar("Angel Di Maria")
print (argentina.jugadores)
print (seleccion.jugadores)
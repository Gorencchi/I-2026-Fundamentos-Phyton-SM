class Seleccion:
    def __init__(self, pais, confederacion):#init es el constructor
        self.jugadores = []
        self.pais = pais
        self.confederacion = confederacion
    def agregar(self, jugador):
        self.jugadores.append(jugador) #agrega jugadores a la lista :pp
    
    def eliminar(self, jugador):
        for jugador_lista in self.jugadores:
            if jugador_lista == jugador:
                self.jugadores.remove(jugador_lista)#borra el jugador
                break
            
pais = input("Ingrese el nombre del país: ")
confederacion = input("Escriba la confederacion: ")
jugador = input("Escriba el nombre del jugador: ")
argentina = Seleccion("Argentina", "CONMEBOL")
brasil = Seleccion("Brasil", "CONMEBOL")
espanna = Seleccion("España", "CONMEBOL")

argentina.agregar("Lionel Messi")
argentina.agregar("Angel Di Maria")
brasil.agregar("Neymar")
Seleccion.agregar(jugador)
espanna.agregar("Lamine Yamal")
espanna.agregar("Gabi")
print(argentina.jugadores)
print(brasil.jugadores)
print (espanna.jugadores)
argentina.eliminar("Angel Di Maria")
print (argentina.jugadores)
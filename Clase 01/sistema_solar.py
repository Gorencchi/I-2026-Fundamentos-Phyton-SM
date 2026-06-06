import turtle
import math

# Configuración de pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Sistema Solar")
pantalla.setup(width=800, height=800)

# Sol mis comentarios
sol = turtle.Turtle()
sol.shape("circle")
sol.color("yellow")
sol.shapesize(2)
sol.penup()
sol.goto(0, 0)

# Planeta 1 - Tierra
tierra = turtle.Turtle()
tierra.shape("circle")
tierra.color("blue")
tierra.shapesize(1)
tierra.penup()

# Planeta 2 - Marte
marte = turtle.Turtle()
marte.shape("circle")
marte.color("red")
marte.shapesize(0.8)
marte.penup()

angulo = 0

# Animación
while True:
    x1 = 150 * math.cos(math.radians(angulo))
    y1 = 150 * math.sin(math.radians(angulo))
    tierra.goto(x1, y1)

    x2 = 250 * math.cos(math.radians(angulo * 0.7))
    y2 = 250 * math.sin(math.radians(angulo * 0.7))
    marte.goto(x2, y2)

    angulo += 2
import turtle

class Immeuble():
    def __init__(self):
        pass

    def MonterEtage(self):
        turtle.setheading(90)
        turtle.forward(60)

class Porte():
    def porteRectangle(self):
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)

class Fenetre():
    def FenetreSimple():
        pass



Porte = Porte()

Porte.porteRectangle()

turtle.done()
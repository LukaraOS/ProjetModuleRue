import turtle

class Objet():
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
    
Porte = Objet()

Porte.porteRectangle()

turtle.done()
import turtle

class NewTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('turtle')
    
    def forward(self, x):
        self.backward(2*x)


nonte = turtle.Turtle()
nonte.forward(100)


nonte = NewTurtle()
nonte.forward(100)

turtle.done()
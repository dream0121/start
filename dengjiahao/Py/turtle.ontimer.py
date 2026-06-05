import turtle
def fun():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
turtle.getscreen().ontimer(fun,1000)
turtle.done()
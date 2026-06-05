import turtle
t = turtle.Turtle()
t.goto(100,100)
turtle.listen()


def huaxian(x,y):
    t.pendown()
    t.goto(x,y)


def cliii(x,y):
    turtle.clearscreen()

turtle.onscreenclick(huaxian,1)
turtle.onscreenclick(cliii,3)
turtle.done()


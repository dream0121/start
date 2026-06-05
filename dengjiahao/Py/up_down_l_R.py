import turtle
t = turtle.Turtle()
t.shape("turtle")
def up():
    t.setheading(90)
    t.forward(100)
def down():
    t.setheading(270)
    t.forward(100)
def left():
    t.setheading(180)
    t.forward(100)
def right():
    t.setheading(0)
    t.forward(100)

turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.done()
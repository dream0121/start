import turtle
gametitle = "小海龟挑战大迷宫"
if __name__ == "__main__":
    turtle.title(gametitle)
    turtle.setup(800, 600)
    turtle.bgpic("image/start.jpeg")
    turtle.colormode(255)
#    level = turtle.numinput("选择难度", "请输入1-3", 1, 1, 3)
  #  levelinit()
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.done()

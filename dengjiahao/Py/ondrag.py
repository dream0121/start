import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
turtle.listen()
def fun(x,y) :
    t.pendown()
    t.goto(x,y)
t.ondrag(fun,1)
turtle.done()
'''
核心区别一句话：
import turtle + t = turtle.Turtle()：t = 小乌龟画笔对象
import turtle as t：t = turtle 整个模块包
二者变量t指代的东西完全不一样。
'''
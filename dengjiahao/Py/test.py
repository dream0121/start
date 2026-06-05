import turtle as t
def funclick(x,y):
    t.clear()
    t.write((x,y),font=('Arial',12,'normal'))
t.onscreenclick(funclick,1)
t.done()

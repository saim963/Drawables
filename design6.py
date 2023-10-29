import turtle
s = turtle.Turtle()
s.speed(10)
s.penup()
s.goto(-200,50)
s.pendown()
def star(turtle,size):
    if size <=10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)

star(s,360)

turtle.done()
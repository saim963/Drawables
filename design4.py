import turtle
import math
p = turtle.Turtle()
p.speed(10)
s=turtle.Screen()
s.bgcolor("black")
p.pencolor("white")
for i in range(2000):
    p.forward(math.sqrt(i))
    p.left(i%90)

turtle.done()
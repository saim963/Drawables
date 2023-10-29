import turtle 
import math

p = turtle.Turtle()
p.speed(10)
s=turtle.Screen()
s.bgcolor("black")
p.pencolor("white")
for i in range(3000):
    p.forward(10)
    p.left(math.sin(i/10)*25)
    p.left(20)

turtle.done()
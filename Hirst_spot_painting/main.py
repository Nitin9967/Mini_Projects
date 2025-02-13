import colorgram
from turtle import Turtle,Screen
import random
colors = colorgram.extract('hirst_painting.jpg', 50)
l = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    l.append(new_color)

t = Turtle()
s = Screen()
s.colormode(255)
def make_dot():
    t.pendown()
    t.dot(20,random.choice(l))
    t.penup()
    t.forward(50)
def change_position(i):
    t.penup()
    t.goto(-250,-250+(50*i))
def make_dot_line():
    for i in range(10):
        # t.color(random.choice(l))
        make_dot()
for i in range(10):
    change_position(i)
    make_dot_line()
t.hideturtle()
t.speed("fastest")
s.exitonclick()

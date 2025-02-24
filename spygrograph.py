from turtle import Turtle,Screen
import random
n = Turtle()
s = Screen()
s.colormode(255)
n.speed("fastest")
def random_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    col_tup = (r,g,b)
    return col_tup
for i in range(100):
    n.pencolor(random_color())
    n.width(5)
    n.circle(200)
    n.right(5)
s.exitonclick()

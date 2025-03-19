from turtle import Turtle, Screen
import time


t = Turtle()
s = Screen()
s.title("Count-Down Timer")
t.hideturtle()
t.penup()
t.goto(0, 0)
t.color("black")
t.write("Timer Starting...", align="center", font=("Arial", 24, "normal"))

def countdown(seconds):
    for i in range(seconds, 0, -1):
        t.clear()
        t.write(f"00:{i}", align="center", font=("Arial", 48, "bold"))
        time.sleep(1)
    t.clear()
    t.write("Time's up!", align="center", font=("Arial", 36, "bold"))

countdown(60)
s.exitonclick()

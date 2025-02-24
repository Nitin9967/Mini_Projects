from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food = Turtle()
        self.shape("circle")
        self.color("Blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.reset()
    def reset(self):
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.pendown()


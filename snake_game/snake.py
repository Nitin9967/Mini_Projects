from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
x_point = 0
y_point = 0
class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()

    def create_snake(self):
         for position in positions:
             self.new_part(position)
    def new_part(self,pos):
        new_part = Turtle()
        new_part.penup()
        new_part.shape("square")
        new_part.color("white")
        new_part.goto(pos)
        self.snake.append(new_part)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x_point = self.snake[i - 1].xcor()
            y_point = self.snake[i - 1].ycor()
            self.snake[i].goto(x_point, y_point)
        self.snake[0].forward(20)
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

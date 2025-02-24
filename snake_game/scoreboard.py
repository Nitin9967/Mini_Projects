from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.score = 0
        self.update_score()
    def update_score(self):
        self.write(f"Score : {self.score}", move=False, align="center", font=('Arial', 25, 'normal'))
    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=('Arial', 25, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


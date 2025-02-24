from turtle import Screen
import food
import snake
import time
import scoreboard
S = snake.Snake()
s = Screen()
s.setup(width=600,height=600)
Score = scoreboard.Scoreboard()
s.listen()
s.onkey(S.up,"Up")
s.onkey(S.down,"Down")
s.onkey(S.right,"Right")
s.onkey(S.left,"Left")
s.tracer(0)
s.bgcolor("black")
s.title("MY SNAKE GAME !!")
food = food.Food()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    S.move()
    if S.snake[0].distance(food)<15:
        food.reset()
        Score.increase_score()
        S.new_part((snake.x_point,snake.y_point))
    if S.snake[0].xcor()>290 or S.snake[0].ycor()>290 or S.snake[0].xcor()<-290 or S.snake[0].ycor()<-290:
        game_is_on = False
        Score.game_over()
    for segment in S.snake[1:]:
        if S.snake[0].distance(segment)<10:
            game_is_on = False
            Score.game_over()




s.exitonclick()
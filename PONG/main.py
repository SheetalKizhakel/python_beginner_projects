from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time
screen=Screen()   #creating the screen
screen.bgcolor("black")
screen.title("Welcome to the pong game!")
screen.setup(width=800,height=600)
screen.tracer(0)
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
screen.listen()
screen.onkey(key="Up",fun=right_paddle.go_up)
screen.onkey(key="Down",fun=right_paddle.go_down)
screen.onkey(key="w",fun=left_paddle.go_up)
screen.onkey(key="s",fun=left_paddle.go_down)
scoreboard1=ScoreBoard()
game_on=True
while game_on==True:
    time.sleep(0.09)
    ball.move_ball()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_away_from_wall()
    if (ball.xcor()>330 and ball.distance(right_paddle)<20) or (ball.xcor()<-330 and ball.distance(left_paddle)<20):
        ball.bounce_away_from_paddle()
    if ball.xcor()>370 and ball.xcor()<400:
        scoreboard1.increase_score_left_paddle()
        ball.refresh()
    if ball.xcor() < -370 and ball.xcor() > -400:
        scoreboard1.increase_score_right_paddle()
        ball.refresh()

    screen.update()

screen.exitonclick()

from turtle import Turtle,Screen
from user import User
from car import Car
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.tracer(0)
user=User()
scoreboard=ScoreBoard()
screen.setup(width=600,height=600)
screen.title("WELCOME TO THE TURTLE CROSSING GAME ! ")
screen.listen()
car = Car()
car.hideturtle()
screen.onkey(key="Up",fun=user.go_forward)
game_on=True
c=6
while game_on:
    time.sleep(0.1)
    if(c%6==0):
        car.create_car()
    car.move_car()
    c=c+1
    for x in car.car_list:
        if user.distance(x)<28:
            game_on=False
            scoreboard.printing_message()

    if user.ycor()>290:
        user.go_back_to_original_position()
        scoreboard.update_score()
        car.change_level()
        if user.distance(x)<28:
            game_on=False
            scoreboard.printing_message()
        if user.ycor() > 290:
            game_on = False
    screen.update()
screen.exitonclick()
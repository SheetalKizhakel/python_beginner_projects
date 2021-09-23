from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_x=10
        self.move_y=10
    def move_ball(self):
        new_x=self.xcor()+self.move_x
        new_y=self.ycor()+self.move_y
        self.penup()
        self.goto(new_x,new_y)

    def bounce_away_from_wall(self):
        self.move_y*=-1

    def bounce_away_from_paddle(self):
        self.move_x*=-1

    def refresh(self):
        self.goto(x=0,y=0)
        self.bounce_away_from_paddle()
        time.sleep(2)




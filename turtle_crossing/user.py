from turtle import Turtle
class User(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0,y=-280)

    def go_forward(self):
        new_x=self.xcor()
        new_y=self.ycor()+10
        self.goto(new_x,new_y)

    def go_back_to_original_position(self):
        self.goto(x=0,y=-280)




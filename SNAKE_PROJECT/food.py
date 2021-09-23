from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.shapesize(0.5,0.5)
    def refresh(self):
        x_coordinate=random.randint(-280,280)
        y_coordinate=random.randint(-280,280)
        self.goto(x=x_coordinate,y=y_coordinate)
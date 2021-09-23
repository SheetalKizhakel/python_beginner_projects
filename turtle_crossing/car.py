LIST_OF_COLORS=['blue','orange','green','brown','magenta','cyan','red','turquoise','gold','crimson','olive']
from turtle import Turtle
import random
class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.car_list=[]
        self.carspeed=10

    def move_car(self):
        for i in range(0,len(self.car_list)):
            self.car_list[i].backward(self.carspeed)
    def create_car(self):
        new_car=Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(LIST_OF_COLORS))
        new_x_coordinate=300
        new_y_coordinate=random.randint(-240,280)
        new_car.goto(new_x_coordinate, new_y_coordinate)
        self.car_list.append(new_car)

    def change_level(self):
        self.carspeed+=5


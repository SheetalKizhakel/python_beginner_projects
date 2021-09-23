STARTING_POSITIONS=[-40, -20, 0]
MOVE_DISTANCE=20
from turtle import Turtle
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_new_snake()

    def create_new_snake(self):
     for i in STARTING_POSITIONS:
           new_segment = Turtle(shape="square")
           new_segment.color("white")
           new_segment.penup()
           new_segment.goto(x=i,y=0)
           self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for x in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[x-1].xcor()
            new_y =self.segments[x-1].ycor()
            self.segments[x].goto(x=new_x,y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):

        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def down(self):

        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)



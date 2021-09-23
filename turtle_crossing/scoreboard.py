from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=1
        self.penup()
        self.goto(x=-260,y=280)
        self.write(f"LEVEL IS : {self.score} ",align='left',font=('Ariel',13,'normal'))
    def printing_message(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER !",align='center',font=('Ariel',20,'normal'))

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"LEVEL IS {self.score} ", align='center', font=('Ariel', 13, 'normal'))

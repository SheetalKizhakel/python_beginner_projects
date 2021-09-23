from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.write(f"Score:{self.score}",move=False,align="center",font=("Arial",22 ,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",move=False,align="center",font=("Arial",22 ,"normal"))
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER")

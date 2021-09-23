from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write("score is",align='center',font=('Arial', 17, 'normal'))
        self.left_paddle_score=0
        self.right_paddle_score=0
        self.goto(x=-100,y=260)
        self.write(f"{self.left_paddle_score}",font=('Arial', 17, 'normal'))
        self.goto(x=100,y=260)
        self.write(f"{self.right_paddle_score}",font=('Arial', 17, 'normal'))

    def increase_score_left_paddle(self):
        self.clear()
        self.left_paddle_score += 1
        self.goto(-100, 200)
        self.write(f"{self.left_paddle_score}", font=('Arial', 17, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.right_paddle_score}", font=('Arial', 17, 'normal'))



    def increase_score_right_paddle(self):
        self.clear()
        self.right_paddle_score+=1
        self.goto(-100, 200)
        self.write(f"{self.left_paddle_score}", font=('Arial', 17, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.right_paddle_score}", font=('Arial', 17, 'normal'))


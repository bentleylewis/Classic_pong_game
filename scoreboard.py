from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        if self.r_score == 5:
            winning_side = "Right"
        elif self.l_score == 5:
            winning_side = "Left"
        self.write(f"{winning_side} Wins!", align='center', font=("Courier", 40, "normal"))
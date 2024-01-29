from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.msg_position = (-20,270)
        self.setpos(self.msg_position)
        self.color("white")
        self.hideturtle()
    
    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align =ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
       
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align =ALIGNMENT, font=FONT)

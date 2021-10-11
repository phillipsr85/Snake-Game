from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier',18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.penup()
        self.goto(0,265)
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()



    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)
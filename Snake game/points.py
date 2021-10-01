import turtle
eaten = 0


class PointsCounter(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.eaten = eaten
        self.penup()
        self.goto(0, 370)
        self.add_score()
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.write(f"SCORE : {self.eaten}", False, "center", ("Arial", 12, "bold"))
        self.eaten += 1

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 22, "bold"))

import turtle
eaten = 0


class PointsCounter(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.eaten = eaten
        self.penup()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 370)
        self.add_score()
        self.hideturtle()

    def add_high_score(self):
        with open("high_score.txt", "w") as file:
            if self.high_score < self.eaten:
                file.write(str(self.eaten - 1))
                self.high_score = self.eaten
            else:
                file.write(str(self.high_score))

    def add_score(self):
        self.clear()
        self.write(f"SCORE : {self.eaten}   HIGH SCORE : {self.high_score}", False, "center", ("Arial", 12, "bold"))
        self.eaten += 1

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 22, "bold"))

    def play_again_screen(self, time):
        self.clear()
        self.goto(0, -30)
        self.write(f"PLAYING AGAIN IN : {time}\n\nOR PRESS ESCAPE TO EXIT", align="center", font=("Arial", 22, "bold"))

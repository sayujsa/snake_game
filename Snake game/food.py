from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.shapesize(.7)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-480, 480), randint(-380, 380))

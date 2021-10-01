import turtle
from turtle import Turtle
import time


class Snake:

    turtle.tracer(1, 0)

    def __init__(self, length, speed):
        self.length = length
        self.speed = speed
        self.snake_pieces = []
        for x in range(0, self.length * -20 + 10, -20):
            pointer = Turtle("square")
            pointer.penup()
            pointer.color("white")
            pointer.setpos(x, 0)
            self.snake_pieces.append(pointer)

    def move(self):
        time.sleep(self.speed)
        for x in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[x - 1].xcor()
            new_y = self.snake_pieces[x - 1].ycor()
            self.snake_pieces[x].goto(new_x, new_y)
        self.snake_pieces[0].forward(20)

    def go_north(self):
        if self.snake_pieces[0].heading() == 0 or self.snake_pieces[0].heading() == 180:
            self.snake_pieces[0].setheading(90)

    def go_south(self):
        if self.snake_pieces[0].heading() == 0 or self.snake_pieces[0].heading() == 180:
            self.snake_pieces[0].setheading(270)

    def go_east(self):
        if self.snake_pieces[0].heading() == 90 or self.snake_pieces[0].heading() == 270:
            self.snake_pieces[0].setheading(0)

    def go_west(self):
        if self.snake_pieces[0].heading() == 90 or self.snake_pieces[0].heading() == 270:
            self.snake_pieces[0].setheading(180)





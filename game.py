import snake_file
import turtle

screen = turtle.Screen()
screen.setup(990, 790)
screen.bgcolor("black")
snake = snake_file.Snake(5, .1)
while True:
    screen.onkeypress(snake.go_north, "Up")
    screen.onkeypress(snake.go_south, "Down")
    screen.onkeypress(snake.go_east, "Right")
    screen.onkeypress(snake.go_west,  "Left")
    screen.listen()
    snake.move()

# screen.exitonclick()

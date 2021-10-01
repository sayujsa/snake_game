import snake_file
import turtle
import food
import points

turtle.tracer(1, 0)
screen = turtle.Screen()
screen.setup(990, 790)
screen.bgcolor("black")
screen.title("SNAKE")
snake = snake_file.Snake(5, .1)
apples = food.Food()
points_taken = points.PointsCounter()
can_play = True

while can_play:
    screen.onkeypress(snake.go_north, "Up")
    screen.onkeypress(snake.go_south, "Down")
    screen.onkeypress(snake.go_east, "Right")
    screen.onkeypress(snake.go_west,  "Left")
    screen.listen()
    snake.move()

    if snake.snake_pieces[0].distance(apples) < 15:
        apples.refresh()
        points_taken.add_score()
        snake.extend()

    if snake.snake_pieces[0].xcor() > 485 or snake.snake_pieces[0].xcor() < -485 or\
            snake.snake_pieces[0].ycor() > 385 or snake.snake_pieces[0].ycor() < -385:
        points_taken.game_over()
        break

    for piece in snake.snake_pieces[1:]:
        if snake.snake_pieces[0].distance(piece) < 10:
            can_play = False
            points_taken.game_over()

screen.exitonclick()

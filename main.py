from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

score.show()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refesh()
        score.score_track()
        snake.extend()
    snake.move()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()










screen.exitonclick()


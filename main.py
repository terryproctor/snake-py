from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.update_scoreboard()
g_snake = Snake()
g_food = Food()

screen.listen()
screen.onkey(g_snake.up, "Up")
screen.onkey(g_snake.down, "Down")
screen.onkey(g_snake.left, "Left")
screen.onkey(g_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    g_snake.move()    

    # Detect collision with food
    # if head collides with food
    if g_snake.head.distance(g_food) < 18:
        scoreboard.increase_score()
        g_food.refresh()
        g_snake.extend()  

    if abs(g_snake.head.xcor()) > 290 or abs(g_snake.head.ycor()) > 290:
        scoreboard.reset()
        g_snake.reset()

    for segment in g_snake.segments[1:]:
        if g_snake.head.distance(segment) < 5:
            scoreboard.reset()
            g_snake.reset()



screen.exitonclick()
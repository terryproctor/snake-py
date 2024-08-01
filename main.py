from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

g_snake = Snake()

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

screen.exitonclick()
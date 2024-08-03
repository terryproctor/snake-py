from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

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
    if g_snake.segments[0].distance(g_food) < 18:
        g_food.refresh()
        #g_snake.extend()  

    if abs(g_snake.segments[0].xcor()) > 280 or abs(g_snake.segments[0].ycor()) > 280:
        game_is_on = False
        print("Game Over")

screen.exitonclick()
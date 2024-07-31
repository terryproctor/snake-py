from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def create_snake_piece():
    snake_piece = Turtle("square")
    snake_piece.color("white")
    snake_piece.penup()
    return snake_piece

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    snake_piece = create_snake_piece()
    snake_piece.goto(position)
    segments.append(snake_piece)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
   
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    segments[0].forward(20)    
        
        



screen.exitonclick()
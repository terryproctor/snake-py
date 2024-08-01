from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):   
        for position in STARTING_POSITIONS:
            snake_piece = Turtle("square")
            snake_piece.color("white")
            snake_piece.penup()
            snake_piece.goto(position)
            self.segments.append(snake_piece)

    def move(self):
        segments = self.segments
        for i in range(len(segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor() 
            new_y = self.segments[i-1].ycor()
            segments[i].goto(new_x, new_y)
        segments[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)    


    

    

    
    
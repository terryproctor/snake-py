from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_piece(self,  position):
        snake_piece = Turtle("square")
        snake_piece.color("white")
        snake_piece.penup()
        snake_piece.goto(position)
        return snake_piece

    def create_snake(self):   
        for position in STARTING_POSITIONS:
            snake_piece = self.create_piece(position)
            self.segments.append(snake_piece)

    def move(self):
        segments = self.segments
        for i in range(len(segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor() 
            new_y = self.segments[i-1].ycor()
            segments[i].goto(new_x, new_y)
        segments[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)   

    def extend(self):
        new_position = self.segments[-1].position()
        snake_piece = self.create_piece(new_position)
        self.segments.append(snake_piece)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    

    
    
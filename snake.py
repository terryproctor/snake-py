from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    
        def create_snake_piece():
            snake_piece = Turtle("square")
            snake_piece.color("white")
            snake_piece.penup()
            return snake_piece
        
        for position in self.starting_positions:
            snake_piece = create_snake_piece()
            snake_piece.goto(position)
            self.segments.append(snake_piece)

    def move(self):
        segments = self.segments
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
            segments[0].forward(20) 


    

    

    
    
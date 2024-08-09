from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

        with open("high_score.txt") as h_score:
            high_score = h_score.read()
            try:
                self.high_score = int(high_score)
            except:
                with open("high_score.txt", "w") as h_score:
                    h_score.write("0")
            h_score.close()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt", "w") as h_score:
                h_score.write(str(self.high_score))
                h_score.close()

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        
    

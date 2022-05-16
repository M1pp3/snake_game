from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        with open("data.txt", 'r') as data:
            self.high_score = int(data.read())
        self.ht()

    def show(self):
        self.goto(0, 260)
        self.score_update()

    def score_track(self):
        self.score += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            hs = open("data.txt", 'w')
            hs.write(str(self.high_score))
            hs.close()
        self.score = 0
        self.score_update()

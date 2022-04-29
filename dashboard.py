from turtle import Screen, Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-270, 120)
        self.color("white")
        self.hideturtle()
        self.level = 1
        self.write(f"Level: {self.level}", False, 'Left', ('Arial', 15, 'normal'))

    def level_up(self):
        self.level += 1
        self.write(f"Level: {self.level}", False, 'Left', ('Arial', 15, 'normal'))

    def lose(self):
        self.penup()
        self.clear()
        self.goto(0, 0)
        self.pendown()
        self.write(f"Lose", False, 'Center', ('Arial', 30, 'normal'))




from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.lane = [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100]
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.color("blue")
        self.goto(300, self.lane[random.randint(0, 10)])
        self.setheading(180)
        self.speed(1)

    def move_forward(self):
        self.forward(5)

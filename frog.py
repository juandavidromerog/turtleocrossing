from turtle import Turtle

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("pink")
        self.y_cor = -120
        self.x_cor = 0
        self.goto(self.x_cor, self.y_cor)
        self.setheading(90)
        self.shapesize(0.5)

    def move_up(self):
        self.y_cor += 20
        self.goto(self.x_cor, self.y_cor)

    def move_right(self):
        self.x_cor += 20
        self.goto(self.x_cor, self.y_cor)

    def move_left(self):
        self.x_cor += -20
        self.goto(self.x_cor, self.y_cor)

    def crash(self, car_coordinates):
        if self.distance(car_coordinates.xcor() - 5, car_coordinates.ycor()) < 15 or self.distance(car_coordinates.xcor() + 40, car_coordinates.ycor()) < 20:
            return True
        return False


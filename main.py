from turtle import Screen
from cars import Cars
from frog import Frog
from dashboard import Scoreboard
import time

time_sleep = 0.008


screen = Screen()
screen.setup(width=600, height=300)
screen.title("Turtle Crossing Street")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

frog = Frog()
scoreboard = Scoreboard()

screen.onkey(frog.move_up, "Up")
screen.onkey(frog.move_right, "Right")
screen.onkey(frog.move_left, "Left")

on_game = True
car_list = []
while on_game:
    i = Cars()
    car_list.append(i)
    for _ in car_list:
        for next in range(0, 6):
            _.move_forward()
            screen.update()
            time.sleep(time_sleep)
        if frog.crash(_):
            scoreboard.lose()
            on_game = False
            screen.update()
    if frog.y_cor > 100:
        time_sleep *= 0.1
        print(time_sleep)
        frog.y_cor = -120
        frog.x_cor = 0
        frog.goto(frog.x_cor, frog.y_cor)
        scoreboard.clear()
        scoreboard.level_up()
        screen.update()


screen.exitonclick()

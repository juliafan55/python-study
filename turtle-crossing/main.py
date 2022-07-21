# create turtle -> make it move across screen on y axis
# create scoreboard -> update as the turtle crosses
# create the cars -> random color, speed increases as the levels go up (as the turtle passes)

from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect turtle has reached the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.add_point()

screen.exitonclick()

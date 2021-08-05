from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=750, height=750)
screen.tracer(0)
player = Player()
screen.tracer(0)
screen.listen()

cars = Cars()
scoreboard = Scoreboard()

game_is_on = True
cars.create_car()
difficulty = scoreboard.level
while game_is_on:

    screen.update()
    time.sleep(.1)
    cars.move_cars()

    for location in cars.car_list:
        if player.distance(location) < 15:
            game_is_on = False
            scoreboard.game_over()

    if difficulty == 10:
        cars.create_car()
        cars.move_cars()
        difficulty = scoreboard.level
    else:
        difficulty += 1

    screen.onkeypress(player.movement, "Up")

    if player.ycor() >= 350:
        player.player_home()
        scoreboard.level_increase()

screen.exitonclick()

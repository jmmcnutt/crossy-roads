from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.speed = 1
        self.penup()
        self.hideturtle()

    def create_car(self):

        x = 0
        new_car = []

        for times in range(3):
            segments = Turtle("square")

            segments.penup()
            segments.setpos(x, y=0)

            x += 20
            new_car.append(segments)

        random_color = random.choice(COLORS)

        for part in range(len(new_car)):
            new_car[part].color(random_color)

        x_coordinate = 350
        y_coordinate = random.randint(-310, 310)

        for parts in new_car:
            new_car[0].setpos(x_coordinate, y_coordinate)
            new_car[1].setpos(x_coordinate + 20, y_coordinate)
            new_car[2].setpos(x_coordinate + 40, y_coordinate)
            self.car_list.append(parts)

    def move_cars(self):

        for parts in self.car_list:

            parts.setheading(180)
            parts.forward(10)

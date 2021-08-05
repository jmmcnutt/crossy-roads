from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.starting_position()

    def starting_position(self):

        self.penup()
        self.goto(x=0, y=-310)
        self.setheading(90)

    def movement(self):

        self.forward(10)

    def player_home(self):

        self.starting_position()
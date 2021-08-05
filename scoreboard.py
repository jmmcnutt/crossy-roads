from turtle import Turtle

FONT = ("Courier New", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.show_level()

    def game_over(self):

        self.hideturtle()
        self.home()
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)

    def show_level(self):

        self.clear()
        self.penup()
        self.color("black")
        self.goto(-275, 320)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_increase(self):

        self.clear()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-275, 320)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

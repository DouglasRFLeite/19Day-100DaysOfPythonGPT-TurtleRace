from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

player_bet = screen.textinput(
    "Make a Bet", f"Which color turtle do you think will win?\n({', '.join(colors)})")

turtles = []
pos = (-220, -90)
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.setpos(pos)
    turtle.pendown()
    turtles.append(turtle)
    print(f"{color} turtle created")
    pos = (pos[0], pos[1] + 30)

while True:
    index = random.randint(0, len(turtles)-1)
    turtles[index].forward(10)
    if turtles[index].xcor() >= 250:
        print(f"The winner is '{turtles[index].color()[0]}'")
        if turtles[index].color()[0] == player_bet:
            print("You win!")
        else:
            print("You lose")
        break


screen.exitonclick()

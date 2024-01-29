import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
turtle_array = []
screen.setup(width=500, height=400)
is_race_on = False
user_input = screen.textinput("Bet", "Choose your turtle")

y = 20
if user_input:
    is_race_on = True
for i in range(0, len(colors)):
    if user_input != colors[i]:
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x=-250, y=y)
        y += 30
        turtle_array.append(t)

user_turtle = Turtle(shape="turtle")
user_turtle.color(user_input)
user_turtle.penup()
user_turtle.goto(x=-250, y=190)
turtle_array.append(user_turtle)


while is_race_on:
    for t in turtle_array:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print("You won!")
            else:
                print(f"Turtle with color {winning_color} won!")
        rand_distance = random.randint(1, 10)
        t.forward(rand_distance)
screen.exitonclick()

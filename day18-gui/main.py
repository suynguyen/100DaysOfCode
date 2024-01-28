import turtle
from turtle import Turtle, Screen
import random

angles = [90, 180, 270]
length = [5, 10, 20, 30, 40]
tim = Turtle()
turtle.colormode(255)
corner = 3


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for y in range(3, 100):
    for i in range(y):
        tim.speed(5)
        tim.width(5)
        tim.color(random_color())
        tim.forward(random.choice(length))
        tim.left(random.choice(angles))

screen = Screen()
screen.exitonclick()

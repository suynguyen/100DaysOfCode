import turtle
from turtle import Turtle, Screen
import random
import colorgram

angles = [90, 180, 270]
length = [5, 10, 20, 30, 40]
tim = Turtle()
turtle.colormode(255)
corner = 3


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_random_moves():
    for y in range(3, 100):
        for i in range(y):
            tim.speed(5)
            tim.width(5)
            tim.color(random_color())
            tim.forward(random.choice(length))
            tim.left(random.choice(angles))


def draw_circle(direction):
    radius = 100
    tim.speed(15)
    tim.color(random_color())
    tim.circle(radius)
    tim.setheading(direction)


rgb_colors = []


def extract_color():
    colors = colorgram.extract("pic.jpg", 100)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_rgb = (r, g, b)
        rgb_colors.append(color_rgb)


def draw_dots():
    extract_color()
    for _ in range(100):
        tim.penup()
        tim.dot(10, random.choice(rgb_colors))
        tim.forward(10)


draw_dots()
screen = Screen()
screen.exitonclick()

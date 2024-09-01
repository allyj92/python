# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("pink")
#
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
#
#
#
#
#
#
# screen = Screen()
# screen.exitonclick()

# from turtle import *
# tim = Turtle();
# tom = Turtle();
# terry = Turtle();
import random
from turtle import Turtle as t, Screen

tim = t()
# tim.shape('turtle')
#
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def draw_random_line():


for shape_side_n in range (3,30):
  change_color()
  draw_shape(shape_side_n)







screen = Screen()
screen.exitonclick()
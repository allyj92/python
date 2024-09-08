import turtle as t
import random
tim = t.Turtle()
tim.speed(11)
t.colormode(255)

def random_color1():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color =(r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color1())
        tim.circle(100)
        # tim.left(5)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(4)
screen = t.Screen()
screen.exitonclick()
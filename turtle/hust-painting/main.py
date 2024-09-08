import turtle
import turtle as t
import random
# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
# #
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
#
#
# red = rgb[0]
# red = rgb.r
# green = rgb.g
# blue = rgb.b
# saturation = hsl[1]
# saturation = hsl.s
#
#
# col_list=[]
# for i in range (len(colors)):
#     color = colors[i]
#     rgb = color.rgb # e.g. (255, 151, 210)
#     r=rgb.r
#     g=rgb.g
#     b=rgb.b
#
#     col_list.append((r,g,b))
# print(col_list)

color_list = [(239, 234, 230), (238, 233, 235), (230, 231, 236), (17, 21, 40), (159, 62, 43), (196, 160, 111), (143, 163, 190), (230, 235, 232), (229, 204, 103), (47, 15, 12), (33, 14, 22), (154, 57, 72), (75, 95, 123), (21, 46, 32), (168, 152, 47), (185, 140, 152), (73, 112, 87), (159, 172, 160), (199, 74, 88), (137, 35, 26), (47, 51, 95), (193, 94, 80), (217, 177, 183), (223, 176, 172), (114, 40, 63), (81, 80, 29), (177, 188, 211), (91, 112, 170), (42, 81, 44), (43, 71, 74)]

random_color = random.choice(color_list)
print(random_color)
t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.setx(-230)
tim.sety(-210)
for _ in range(10):
    for _ in range(10):

        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.right(90)

tim.hideturtle()






screen = t.Screen()
screen.exitonclick()


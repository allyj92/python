# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# import turtle
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

import prettytable

from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle","Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name",["Pikachu", "Squirtle" ,"Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"

table.align = "l";

print(table)

print(table)
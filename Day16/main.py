# from turtle import Turtle, Screen
from prettytable import PrettyTable

# myTurtle = Turtle()
# print(myTurtle)
# myTurtle.shape("turtle")
# myTurtle.fd(150)

# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()


table = PrettyTable()
table.add_column("City Name",["Hong Kong","London"])
table.add_column("Country",["Hong Kong","UK"])
print(table.align)
table.align = "l"
print(table)

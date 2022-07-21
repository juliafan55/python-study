# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"

# print(table)

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed("fastest")

# for line in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# for line in range(50):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.pendown()

colors = ["red", "black", "coral", "blue"]


# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for line in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shapes(shape_side_n)

# directions = [0, 90, 180, 270]
# timmy.pensize(10)

# for line in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(20)
#     timmy.setheading(random.choice(directions))

# def draw(size_of_the_gap):
#     for line in range(int(360 / size_of_the_gap)):
#         timmy.circle(100)
#         current_heading = timmy.heading()
#         timmy.setheading(current_heading + size_of_the_gap)


# draw(5)

screen = Screen()
screen.exitonclick()

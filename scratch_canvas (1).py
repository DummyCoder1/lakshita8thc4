import turtle
width = int(input('Enter the widhh'))
length = int(input('Enter the length'))
for variable in range(0, 2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

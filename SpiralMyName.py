# SpiralMyName.py - prints a colerful spiral of the user's name


import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]



your_name = turtle.textinput("Enter your name", "What is your name?")



for x in range(300):
    t.pencolor(colors[x%4]) #Rotate through the four colors
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(92)              # Turn left, just as in our other spirals
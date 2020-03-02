# This is a module which might be helpful in class definition

import turtle

# function to draw a square shape
def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle() # brad is an instance of the class Turtle
    brad.shape("turtle")
    brad.speed(2)
    temp1=0

    
    while(temp1<4):
        brad.forward(100)
        brad.right(90)
        temp1=temp1+1

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("red")
    # angie.circle(100)
    # angie.speed(2 )

    window.exitonclick()

draw_square()

# making multiple squares as in UDACITY course using class Turtle
import turtle

window = turtle.Screen()
window.bgcolor("white")

brad = turtle.Turtle() # brad is an instance of the class Turtle
brad.shape("turtle")
brad.speed(10)

# definition of a function to draw a square
#---------------------------------------------#

def make_square(instin):
    temp1=0
    while(temp1<4):
        instin.forward(100)
        instin.right(90)
        temp1=temp1+1
#---------------------------------------------#

for var1 in range(0,30):
    turn_ang = 12
    brad.right(turn_ang)
    make_square(brad)



window.exitonclick()

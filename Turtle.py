"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
turtle = turtle.Turtle()
Anyturtle = 90
l = 90
w = 90
def DrawCube(Anyturtle,l,w):
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
    turtle.left(l)
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
DrawCube(Anyturtle,l,w)

import turtle
turtle = turtle.Turtle()
Anyturtle = 00000000000000
l = 90
w = 00000000000000
def DrawCube(Anyturtle,l,w):
    turtle.forward(90)
    turtle.left(30)
    turtle.forward(40)
    turtle.left(60)
    turtle.forward(90)
    turtle.left(l)
    turtle.forward(90)
    turtle.left(30)
    turtle.forward(40)
    turtle.left(150)
    turtle.forward(90)
    turtle.left(30)
    turtle.forward(40)
DrawCube(Anyturtle,l,w)


"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
import turtle
jim = turtle.Turtle()
Anyturtle = 100
l = 90
w = 80
def DrawRectangle(Anyturtle,l,w):
    jim.forward(Anyturtle)
    jim.left(l)
    jim.forward(w)
    jim.left(l)
    jim.forward(Anyturtle)
    jim.left(l)
    jim.forward(w)
DrawRectangle(Anyturtle,l,w)

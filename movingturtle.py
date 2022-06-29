import turtle as t
import random as rd
import time as ti

# This is for defining the window space for the turtle to move in

def inside_window():
    left_limit = (-t.window_width()/2) + 100
    right_limit = (t.window_width()/2) - 100
    top_limit = (t.window_width()/2) - 100
    bottom_limit = (-t.window_width()/2) + 100
    (x,y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

#This defines the movement of the turtle in the box

def move_turtle():
    if inside_window():
        angle = rd.randint(0,180)
        t.right(angle)
        t.forward(200)
    else:
        t.backward(200)


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('slow')


while True:
    move_turtle()

import turtle as t
import time as ti
from itertools import cycle


colors = cycle(['red', 'green','blue','yellow','orange','grey','purple','pink'])

def circle(size,angle,forw,shape): #this is for defining how the shapes are supposed to be formed
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle': #This is a condition for interating between the cirsle and square
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):#This is for the formation of the square
            t.forward(size*2)
            t.left(90)
        next_shape='circle'
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+1,next_shape) #the is the recursion effect of calling a function in a function


t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30,0,1,'circle')

ti.sleep(2)
t.hideturtle()

import turtle as t
import time as ti

def rec(hor,ver,col): #This is function for defining the rectangles that form the robot
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range (1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed(250) #this is for the speed in my robot
t.bgcolor('Dodger blue') #this is for defining the beckground color

t.goto(-100,-150)
rec(50,20,'blue') #this is  for the first rectangle in the robot system
t.goto(-30,-150)
rec(50,20,'blue')

t.goto(-25,-50)
rec(15,100,'grey')#This is the leg of the robot
t.goto(-70,-50)
rec(15,100,'grey')#this is the leg of the robot

t.goto(-90,100)
rec(100,150,'red')#This the body of the robot

t.goto(-150,70)
rec(60,15,'grey')#this is the arm of the robot
t.goto(-150,110)
rec(15,40,'grey')#This is for the arm of the robot

t.goto(10,70)
rec(60,15,'grey')#this is the arm of the robot
t.goto(55,110)
rec(15,40,'grey')#This is for the arm of the robot
t.goto(-50,120)
rec(15,20,'grey')#This is for the neck of the robot

t.goto(-85,170)
rec(80,50,'red')#This is for the head of the robot

t.goto(-60,160)
rec(30,10,'white')# This is for eyes of the robot
t.goto(-60,160)
rec(5,5,'black')# This is for eyes of the robot
t.goto(-45,155)
rec(5,5,'black')# This is for eyes of the robot

t.goto(-65,135)
t.right(5)
rec(40,5,'black')#this is for the mouth of the robot

#This is for creating the fingers of the robot
t.goto(-155,130)
rec(25,25,'green')
t.goto(-147,130)
rec(10,15,'Dodger blue')

#This is for creating the fingers of the robot
t.goto(50,130)
rec(25,25,'green')
t.goto(58,130)
rec(10,15,'Dodger blue')

t.hideturtle()
ti.sleep(10)

t.hideturtle()#this is for hiding the cursor

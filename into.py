import turtle as t
t.pendown()
t.penup()
t.goto(-250,250)
t.forward(100)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.right(90)
t.right(90)
t.right(90)
t.right(90)
t.forward(100)
t.left(90)
t.right(90)
t.right(90)
t.forward(100)
for i in range(1,5):
    t.forward(200)
    t.right(90)

t.penup()
t.goto(0,0)
t.pendown()
t.color('red')
t.circle(50)
t.circle(150)

t.color('blue')
t.speed(100)
for i in range(1,181):
    t.circle(i)

t.goto(20,-30)
t.color('red')
t.speed(100)
for i in range(1,90):
    t.circle(i)

t.goto(150,250)
for i in range(1,10):
    t.circle(i+90)
    t.left(10)

t.goto(150,-250)
for i in range(1,10):
    t.forward(150)
    t.left(135)

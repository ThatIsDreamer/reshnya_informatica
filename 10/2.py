from turtle import *

ends = []
iter = int(input())
t = Turtle()
t.hideturtle()
tracer(0)
t.speed(0)

length = 300
height = length // 1.618
width = 10
dot = 20
t.width(10)

t.fd(length // 2)
t.right(90)
t.fd(height // 2)
t.dot(dot)
ends.append(t.pos())
t.right(180)
t.fd(height)
t.dot(dot)
ends.append(t.pos())
t.pu()
t.home()
t.pd()

t.left(180)
t.fd(length // 2)
t.right(90)
t.fd(height // 2)
t.dot(dot)
ends.append(t.pos())
t.right(180)
t.fd(height)
t.dot(dot)
ends.append(t.pos())


for i in range(iter):
    new = []
    length //= 2
    
    height = length // 1.618
    width -= 2
    dot -= 2

    t.width(width=width)

    for el in ends:


        t.pu()
        t.goto(el)
        t.setheading(0)
        t.pd()

        t.fd(length // 2)
        t.right(90)
        t.fd(height // 2)
        t.dot(dot)
        new.append(t.pos())
        t.right(180)
        t.fd(height)
        t.dot(dot)
        new.append(t.pos())
        t.pu()
        t.goto(el)
        t.setheading(0)
        t.pd()

        t.left(180)
        t.fd(length // 2)
        t.right(90)
        t.fd(height // 2)
        t.dot(dot)
        new.append(t.pos())
        t.right(180)
        t.fd(height)
        t.dot(dot)
        new.append(t.pos())
    ends = new


done()

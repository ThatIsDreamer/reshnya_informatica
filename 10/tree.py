from turtle import *

ends = []
iter = int(input())

t = Turtle()
t.hideturtle()
t.left(90)
t.width(10)
t.fd(120)
ans = list(t.pos())
ans.append(t.heading())
ends.append(ans)
length = 120
width = 10
t.speed(0)
for i in range((2 ** iter) // 2):
    new = []
    length //= 2
    width -= 2
    for el in ends:
        t.width(width=width)
        t.pu()
        t.goto(el[0], el[1])
        t.seth(el[2])
        t.pd()
        t.left(40)
        t.fd(length)

        ans = list(t.pos())
        ans.append(t.heading())
        new.append(ans)


        t.pu()
        t.goto(el[0], el[1])
        t.seth(el[2])
        t.pd()
        t.right(40)
        t.fd(length)

        ans = list(t.pos())
        ans.append(t.heading())
        new.append(ans)

    ends = new


done()

from turtle import *
color_main, color_remove = input().split()
iteration = int(input())

t = Turtle()

t.speed(0) 
t.hideturtle()
tracer(0)

x0, y0 = -300, 300
length = 600

if iteration == 0:
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.fillcolor(color_main)
    t.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()
else:
    stack = [(x0, y0, length, iteration)]

    while stack:
        x, y, length, iter_count = stack.pop()
        if iter_count == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.fillcolor(color_main)
            t.begin_fill()
            for _ in range(4):
                t.forward(length)
                t.right(90)
            t.end_fill()
        else:
            step = length / 3
            for i in range(3):
                for j in range(3):
                    new_x = x + i * step
                    new_y = y - j * step
                    if i == 1 and j == 1:
                        t.penup()
                        t.goto(new_x, new_y)
                        t.pendown()
                        t.fillcolor(color_remove)
                        t.begin_fill()
                        for _ in range(4):
                            t.forward(step)
                            t.right(90)
                        t.end_fill()
                    else:
                        stack.append((new_x, new_y, step, iter_count - 1))
done()

num3.py

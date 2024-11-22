from math import sin, cos, radians
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

class Fractal:
    SCREEN_SIZE = [600, 600]

    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Polygon Rotation")
        self.angle = 0
        self.mode = 1
        self.start = [0, 0]
        self.length = 2
        self.depth = 1
        self.master.bind('+', self.plus_func)
        self.master.bind('-', self.minus_func)

        file = "GRASS2.FRA"
        self.theo = {}
        with open(file, mode='r') as f:
            lines = [el.strip("\n") for el in f.readlines()]
            self.name = lines[0]
            self.angle = 360 // int(lines[1])
            self.acs = lines[2]
            for el in lines[3:]:
                self.theo[el.split()[0]] = el.split()[1]

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.statestack = []

        self.build(self.depth)
        self.update_display()

        self.master.mainloop()

    def plus_func(self, event):
        self.depth += 1
        self.build(self.depth)
        self.update_display()

    def minus_func(self, event):
        self.depth = max(1, self.depth - 1)
        self.build(self.depth)
        self.update_display()

    def build(self, n=0):
        self.image = Image.new("RGB", self.SCREEN_SIZE, "white")
        self.draw = ImageDraw.Draw(self.image)

        self.cx, self.cy = self.screen(self.start)

        func = self.acs
        for _ in range(n):
            temp = ""
            for el in func:
                temp += self.theo.get(el, el)
            func = temp

        print(func)

        angle = 0
        for el in func:
            if el == "-":
                angle -= self.angle
            elif el == "+":
                angle += self.angle
            elif el == "F":
                x2 = self.cx + self.length * cos(radians(angle))
                y2 = self.cy + self.length * sin(radians(angle))
                self.draw.line((self.cx, self.cy, x2, y2), fill="black")
                self.cx, self.cy = x2, y2
            elif el == "[":
                self.statestack.append((self.cx, self.cy, angle))
            elif el == "]":
                self.cx, self.cy, angle = self.statestack.pop()
            elif el == "|":
                angle += 180

    def update_display(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def cartesian(self, point):
        return point[0] - self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2 - point[1]

    def screen(self, point):
        return point[0] + self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2 - point[1]

Fractal()
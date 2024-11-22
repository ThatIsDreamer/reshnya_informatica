from math import sin, cos, radians, pi
import tkinter


class Movement_Polygon:
    SCREEN_SIZE = [700, 700]

    def __init__(self):
        self.master = tkinter.Tk()
        self.master.title("Polygon Rotation")
        self.angle = 0
        self.mode = 1
        self.cx = self.SCREEN_SIZE[0] // 2
        self.cy = self.SCREEN_SIZE[1] // 2  

        self.main_frame = tkinter.Frame(self.master)
        self.main_frame.pack(side=tkinter.LEFT)

        self.canvas = tkinter.Canvas(self.main_frame, width=self.SCREEN_SIZE[0], height=self.SCREEN_SIZE[1], bg="white")

        self.cx, self.cy = self.screen([100, 0])
        print(self.cx, self.cy)
        self.canvas.create_oval((self.cx - 2, self.cy - 2, self.cx + 2, self.cy + 2))
        self.canvas.pack()
        self.points = []
        self.polygon = None
        self.center = (0, 0)
        self.xformula = "(1 + cos(t)) * cos(t)"
        self.yformula = "(1 + cos(t)) * sin(t)"
        self.build()


        self.rotate_polygon(30)
        self.scale(2)

        self.canvas.create_line(self.SCREEN_SIZE[0] // 2, 0, self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1])
        self.canvas.create_line(0, self.SCREEN_SIZE[1] // 2, self.SCREEN_SIZE[0], self.SCREEN_SIZE[1] // 2)

        self.master.mainloop()

    def build(self):
        angle = 0
        while radians(angle) < 2 * pi:
            t = radians(angle)
            x = eval(self.xformula) * 100
            y = eval(self.yformula) * 100
            self.points.append(self.screen([x, y]))
            angle += 1

        self.canvas.create_polygon(*self.points, outline='blue', fill="")


    def cartesian(self, point):
        return point[0] - self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2 - point[1]

    def screen(self, point):
        return point[0] + self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2 - point[1]

    def rotate_polygon(self, angle=10):
        if not self.points:
            return

        radians_var = radians(angle)

        rotated_points = []

        for x, y in self.points:
            translated_x = x - self.cx
            translated_y = y - self.cy

            rotated_x = translated_x * cos(radians_var) - translated_y * sin(radians_var)
            rotated_y = translated_x * sin(radians_var) + translated_y * cos(radians_var)

            final_x = rotated_x + self.cx
            final_y = rotated_y + self.cy

            rotated_points.append((final_x, final_y))

        #self.points = rotated_points
        self.canvas.delete(self.polygon)
        self.canvas.create_polygon(*rotated_points, outline='green', fill="")

    def scale(self, amount):
        coords = []
        self.cx, self.cy = self.screen([0, 0])
        for i in range(len(self.points)):
            xp, yp = self.cx, self.cy
            xq, yq = self.points[i]
            coords.append((amount * (xq - xp) + xp, amount * (yq - yp) + yp))

        coords.append((amount * (xq - xp) + xp, amount * (yq - yp) + yp))
        self.canvas.delete(self.polygon)
        self.canvas.create_polygon(*coords, fill='', outline='red')
        #self.points = coords


Movement_Polygon()
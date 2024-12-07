from PIL import Image, ImageTk, ImageOps
import tkinter as tk
import datetime
import os

class Mandelbrot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Множество Мандельброта")

        self.xa, self.ya, self.xb, self.yb = -2.0, -1.0, 1.0, 1.0
        self.max_iteration = 255
        self.img_x, self.img_y = 480, 320
        self.image = None
        self.pal = []
        self.currpal = 12
        # Border settings
        self.border_thickness = 5
        self.border_color = "red"
        self.border_width = 100
        self.border_height = 60
        self.history = [[self.xa, self.ya, self.xb, self.yb]]

        # Initial position of the border
        self.border_x = 190
        self.border_y = 130

        palette_file = 'pals/' + os.listdir("pals")[self.currpal]
        self.load_palette(palette_file)

        self.build_mandelbrot()


        self.tk_image = ImageTk.PhotoImage(self.image)


        self.canvas = tk.Canvas(self.root, width=self.img_x, height=self.img_y)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.canvas.pack()
        self.expanded = False

        self.root.bind('<p>', self.cycle)
        self.root.bind('<s>', self.save_image)
        self.border = self.draw_border()
        self.root.bind('<Up>', self.move_up)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)

        self.root.bind('<Return>', self.expand)
        self.root.bind('<Escape>', self.go_back)

    def go_back(self, event):
        self.xa, self.ya, self.xb, self.yb = self.history.pop()
        self.build_mandelbrot()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.border = self.draw_border()
        self.canvas.pack()



    def draw_border(self):
        return self.canvas.create_rectangle(
            self.border_x,
            self.border_y,
            self.border_x + self.border_width,
            self.border_y + self.border_height,
            outline=self.border_color,
            width=self.border_thickness
        )

    def update_border(self):
        self.canvas.coords(
            self.border,
            self.border_x,
            self.border_y,
            self.border_x + self.border_width,
            self.border_y + self.border_height
        )
    def expand(self, event):
        self.build_mandelbrot(True)

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.border = self.draw_border()
        self.canvas.pack()


    def save_image(self, event):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("save", exist_ok=True)
        file_name = "save/" + formatted_time + ".png"
        self.image.save(file_name)
        print(f"Сохранено как {file_name}")

    def cycle(self, event):
        self.pal = []
        self.currpal += 1
        self.canvas.delete('all')

        print("Строю ...")
        palette_file = 'pals/' + os.listdir("pals")[self.currpal]
        self.load_palette(palette_file)
        self.build_mandelbrot()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.border = self.draw_border()

        self.canvas.pack()

        print("Готово!")

    def load_palette(self, file_path):
        with open(file_path, mode='r') as f:
            for el in f.readlines():
                el = el.rstrip("\n").split()
                nums = (int(el[0]), int(el[1]), int(el[2]))
                self.pal.append(nums)

    def build_mandelbrot(self, zoom=False):
        if zoom:
            print("ZOOMING")
            x_range = self.xb - self.xa
            y_range = self.yb - self.ya
            xa = self.xa + x_range * self.border_x / self.img_x
            xb = self.xa + x_range * (self.border_x + self.border_width) / self.img_x
            ya = self.ya + y_range * self.border_y / self.img_y
            yb = self.ya + y_range * (self.border_y + self.border_height) / self.img_y
            self.history.append([self.xa, self.ya, self.xb, self.yb])
            self.xa, self.ya, self.xb, self.yb = xa, ya, xb, yb
            print(self.xa, self.ya, self.xb, self.yb)
            print(self.xa, self.ya, self.xb, self.yb)

        self.image = Image.new("RGB", (self.img_x, self.img_y))
        for y in range(self.img_y):
            zy = y * (self.yb - self.ya) / self.img_y + self.ya
            for x in range(self.img_x):
                zx = x * (self.xb - self.xa) / self.img_x + self.xa
                c, z = zx + zy * 1j, 0
                for i in range(self.max_iteration):
                    if abs(z) > 2.0:
                        self.image.putpixel((x, y), self.pal[i])
                        break
                    z = z * z + c


    def move_up(self, event):
        if self.border_y > 0:
            self.border_y -= 10
            self.update_border()

    def move_down(self, event):
        if self.border_y + self.border_height < self.img_y:
            self.border_y += 10
            self.update_border()

    def move_left(self, event):
        if self.border_x > 0:
            self.border_x -= 10
            self.update_border()

    def move_right(self, event):
        if self.border_x + self.border_width < self.img_x:
            self.border_x += 10
            self.update_border()


    def run(self):
        self.root.mainloop()


Mandelbrot().run()

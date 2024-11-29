from PIL import Image, ImageTk
import tkinter as tk
import datetime
import os
class Mandelbrot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mandelbrot Set")

        self.xa, self.ya, self.xb, self.yb = -2.0, -1.0, 1.0, 1.0
        self.max_iteration = 255
        self.img_x, self.img_y = 480, 320
        self.image = None
        self.pal = []
        self.currpal = 0

        palette_file = 'pals/' + os.listdir("pals")[self.currpal]
        self.load_palette(palette_file)

        self.build_mandelbrot()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(self.root, width=self.img_x, height=self.img_y)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.root.bind('<p>', self.cycle)
        self.root.bind('<s>', self.save_image)

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
        self.canvas.pack()

        print("Готово!")

    def load_palette(self, file_path):
        with open(file_path, mode='r') as f:
            for el in f.readlines():
                el = el.rstrip("\n").split()
                nums = (int(el[0]), int(el[1]), int(el[2]))
                self.pal.append(nums)

    def build_mandelbrot(self):
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

    def run(self):
        self.root.mainloop()


Mandelbrot().run()

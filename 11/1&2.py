from PIL import Image
import random


class Mandelbrot:
    def __init__(self):
        self.xa, self.ya, self.xb, self.yb = [-2.0, -1.0, 1.0, 1.0]
        # self.xa, self.ya, self.xb, self.yb = [-1.0, 0.16666666667, -0.5, 0.5]
        # self.xa, self.ya, self.xb, self.yb = [-0.8, 0.1333333333333333, -0.7, 0.2]
        self.max_iteration = 255
        self.file = 'pals/' + input("Введи название файла с палитрой:")
        self.pal = []
        with open(self.file, mode='r') as f:
            for el in f.readlines():
                el = el.rstrip("\n").split()
                nums = (int(el[0]), int(el[1]), int(el[2]))
                self.pal.append(nums)



        self.img_x, self.img_y = 480, 320

    def build(self):
        self.img_x, self.img_y = 480, 320
        image = Image.new("RGB", (self.img_x, self.img_y))
        for y in range(self.img_y):
            zy = y * (self.yb - self.ya) / self.img_y + self.ya
            for x in range(self.img_x):
                zx = x * (self.xb - self.xa) / (self.img_x) + self.xa
                c, z = zx + zy * 1j, 0
                for i in range(self.max_iteration):
                    # если модуль числа превысил 2, то ставим точку с некоторым цветом
                    if abs(z) > 2.0:
                        # image.putpixel((x, y), (i, i, i))
                        # image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
                        image.putpixel((x, y), self.pal[i])
                        break
                    # вычислим следующий элемент последовательности
                    z = z * z + c
        image.show()


Mandelbrot().build()
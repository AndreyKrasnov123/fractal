# import subprocess
#
# libraries = ['numpy', 'matplotlib', 'customtkinter']
# for lib in libraries:
#     subprocess.call(['pip', 'install', lib])

import numpy as np
import matplotlib.pyplot as plt


class FractalViewer:
    def __init__(self):
        pass

    # Функция для генерации фрактала Мандельброта
    def mandelbrot(self, c, max_iter):
        z = 0
        n = 0
        while abs(z) <= 2 and n < max_iter:
            z = z * z + c
            n += 1
        return n

    # Функция для отображения фрактала Мандельброта
    def draw_mandelbrot(self, value_fractal, choice_theme):
        x_min, x_max = -2.5, 2.5
        y_min, y_max = -2.5, 2.5
        resolution = value_fractal
        max_iter = 100
        x = np.linspace(x_min, x_max, resolution)
        y = np.linspace(y_min, y_max, resolution)
        mandelbrot_set = np.zeros((resolution, resolution))
        for i in range(resolution):
            for j in range(resolution):
                mandelbrot_set[i, j] = self.mandelbrot(complex(x[j], y[i]), max_iter)
        plt.imshow(mandelbrot_set.T, extent=(x_min, x_max, y_min, y_max), cmap=choice_theme)
        plt.colorbar()
        plt.show()

# # Пример использования класса FractalViewer
# viewer = FractalViewer()
# value_fractal = 500  # Задаем значение переменной value_fractal
# choice_theme = 'hot'  # Пример значения для choice_theme
# viewer.draw_mandelbrot(value_fractal, choice_theme)

import subprocess

libraries = ['numpy', 'matplotlib', 'customtkinter']
for lib in libraries:
    subprocess.call(['pip', 'install', lib])

import customtkinter
from fracial_generation import FractalViewer


class CustomFractalApp:
    def __init__(self):
        self.value_fractal = 34567890
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        self.app = customtkinter.CTk()
        self.app.geometry("700x460")

    def button_function(self, value_fractal, choice_theme):
        viewer = FractalViewer()
        viewer.draw_mandelbrot(value_fractal, choice_theme)
        print("button pressed")

    def change_text(self):
        new_text = "Новый текст"
        self.variable.set(new_text)

    def combobox_callback(self, choice):
        print("Вы выбрали эту тему в matplotlib:", choice)
        global choice_theme
        self.choice_theme = choice

    def slider_event(self, value):
        self.value_fractal = int(value)
        self.value_label.configure(text=f'Разрешение фрактала : {self.value_fractal} x {self.value_fractal}')

    def run_app(self):
        label_s = customtkinter.CTkLabel(self.app, text="Фрактальный мир", fg_color="transparent")
        label_s.place(relx=0.5, rely=0.07, anchor=customtkinter.CENTER)

        button = customtkinter.CTkButton(master=self.app, text="Генерация фрактала",
                                         command=lambda: self.button_function(self.value_fractal, self.choice_theme))
        button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        slider = customtkinter.CTkSlider(self.app, from_=500, to=5000, width=500, command=self.slider_event)
        slider.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        label = customtkinter.CTkLabel(self.app,
                                       text="500x500 пикселей                                                                    5000x5000 пикселей",
                                       fg_color="transparent")
        label.place(relx=0.5, rely=0.74, anchor=customtkinter.CENTER)
        #
        self.value_label = customtkinter.CTkLabel(self.app, text='Разрешение фрактала: {}'.format(slider.get()))
        self.value_label.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        combobox = customtkinter.CTkComboBox(master=self.app,
                                             values=['Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral',
                                                     'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r',
                                                     'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
                                                     'afmhot_r',
                                                     'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r',
                                                     'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r',
                                                     'cubehelix', 'cubehelix_r', 'flag', 'flag_r'],
                                             command=self.combobox_callback)
        combobox.pack(padx=50, pady=70, ipadx=100)
        combobox.set("Выберите тему   фрактала")  # set initial value

        self.app.mainloop()


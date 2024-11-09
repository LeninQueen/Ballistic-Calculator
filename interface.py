import tkinter as tk
from tkinter import messagebox
from ballistics import calculate_ballistics, plot_trajectory
import numpy as np


class BallisticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчет траектории снаряда")

        # Создание виджетов
        self.create_widgets()

    def create_widgets(self):
        # Элементы интерфейса
        self.velocity_label = tk.Label(self.root, text="Начальная скорость (м/с):")
        self.velocity_label.grid(row=0, column=0, padx=10, pady=5)
        self.velocity_entry = tk.Entry(self.root)
        self.velocity_entry.grid(row=0, column=1, padx=10, pady=5)

        self.mass_label = tk.Label(self.root, text="Масса снаряда (г):")
        self.mass_label.grid(row=1, column=0, padx=10, pady=5)
        self.mass_entry = tk.Entry(self.root)
        self.mass_entry.grid(row=1, column=1, padx=10, pady=5)

        self.diameter_label = tk.Label(self.root, text="Диаметр снаряда (мм):")
        self.diameter_label.grid(row=2, column=0, padx=10, pady=5)
        self.diameter_entry = tk.Entry(self.root)
        self.diameter_entry.grid(row=2, column=1, padx=10, pady=5)

        self.angle_label = tk.Label(self.root, text="Угол (градусы):")
        self.angle_label.grid(row=3, column=0, padx=10, pady=5)
        self.angle_entry = tk.Entry(self.root)
        self.angle_entry.grid(row=3, column=1, padx=10, pady=5)

        self.height_label = tk.Label(self.root, text="Начальная высота (м):")
        self.height_label.grid(row=4, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=4, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Рассчитать", command=self.calculate)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            # Считываем входные данные
            initial_velocity = float(self.velocity_entry.get())
            mass = float(self.mass_entry.get()) / 1000  # конвертируем из грамм в килограммы
            diameter = float(self.diameter_entry.get()) / 1000  # конвертируем из мм в метры
            angle_deg = float(self.angle_entry.get())
            initial_height = float(self.height_entry.get() or 0)

            if not (0 <= angle_deg <= 90):
                raise ValueError("Угол должен быть в диапазоне от 0 до 90 градусов.")

            # Площадь поперечного сечения снаряда
            cross_sectional_area = np.pi * (diameter / 2) ** 2

            # Переводим угол в радианы
            angle_rad = np.radians(angle_deg)

            # Расчёт траектории
            trajectory = calculate_ballistics(initial_velocity, mass, angle_rad, cross_sectional_area, initial_height)

            # Построение графика
            plot_trajectory(trajectory, initial_velocity, mass, angle_deg, diameter)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = BallisticsApp(root)
    root.mainloop()
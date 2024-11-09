import numpy as np
import matplotlib.pyplot as plt

GRAVITY = 9.81  # м/с^2
AIR_DENSITY = 1.2  # кг/м^3
DRAG_COEFFICIENT = 0.295
TIME_STEP = 0.01  # с

def plot_trajectory(trajectory, initial_velocity, mass, angle_deg, diameter, color='b'):
    positions, _ = trajectory

    plt.plot(positions[:, 0], positions[:, 1], label='Траектория снаряда', color=color)
    plt.xlabel('Дальность (м)')
    plt.ylabel('Высота (м)')
    plt.title('Траектория снаряда')
    plt.grid(True)

    plt.scatter(positions[0, 0], positions[0, 1], color='red', zorder=5)
    plt.scatter(positions[-1, 0], positions[-1, 1], color='red', zorder=5)

    plt.annotate('Старт', (positions[0, 0], positions[0, 1]), textcoords="offset points", xytext=(-10, -10),
                 ha='center')
    plt.annotate('Падение', (positions[-1, 0], positions[-1, 1]), textcoords="offset points", xytext=(-10, -10),
                 ha='center')

    plt.text(0.05, 0.95,
             f'Начальная скорость: {initial_velocity:.2f} м/с\nМасса снаряда: {mass:.3f} кг\nУгол: {angle_deg:.2f} градусов\nДиаметр: {diameter:.3f} м',
             verticalalignment='top', horizontalalignment='left', transform=plt.gcf().transFigure, fontsize=10)

    plt.legend()
    plt.show()


def calculate_ballistics(initial_velocity, mass, angle_rad, cross_sectional_area, initial_height=0):
    if initial_velocity <= 0:
        raise ValueError("Начальная скорость должна быть положительным числом.")
    if mass <= 0:
        raise ValueError("Масса снаряда должна быть положительным числом.")

    velocity_x = initial_velocity * np.cos(angle_rad)
    velocity_y = initial_velocity * np.sin(angle_rad)

    positions = []
    drag_constants = 0.5 * DRAG_COEFFICIENT * AIR_DENSITY * cross_sectional_area / mass

    x, y = 0, initial_height
    while y >= 0:
        speed_sq = velocity_x ** 2 + velocity_y ** 2
        drag_force = drag_constants * speed_sq
        acceleration_x = -drag_force * velocity_x / np.sqrt(speed_sq)
        acceleration_y = -GRAVITY - drag_force * velocity_y / np.sqrt(speed_sq)
        velocity_x += acceleration_x * TIME_STEP
        velocity_y += acceleration_y * TIME_STEP
        x += velocity_x * TIME_STEP
        y += velocity_y * TIME_STEP
        positions.append([x, y])

    return np.array(positions), None
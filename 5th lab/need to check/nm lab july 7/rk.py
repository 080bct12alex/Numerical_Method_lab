import numpy as np
import matplotlib.pyplot as plt

def dydx(x, y, z):
    return z

def dzdx(x, y, z):
    return x**2 - y

def rk4(x0, y0, z0, xn, h):
    n = int((xn - x0) / h)
    x = x0
    y = y0
    z = z0
    x_rk4 = [x]
    y_rk4 = [y]
    z_rk4 = [z]
    for i in range(n):
        k1 = h * dydx(x, y, z)
        l1 = h * dzdx(x, y, z)
        k2 = h * dydx(x + h/2, y + k1/2, z + l1/2)
        l2 = h * dzdx(x + h/2, y + k1/2, z + l1/2)
        k3 = h * dydx(x + h/2, y + k2/2, z + l2/2)
        l3 = h * dzdx(x + h/2, y + k2/2, z + l2/2)
        k4 = h * dydx(x + h, y + k3, z + l3)
        l4 = h * dzdx(x + h, y + k3, z + l3)
        z = z + (l1 + 2*l2 + 2*l3 + l4) / 6
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        x_rk4.append(x)
        y_rk4.append(y)
        z_rk4.append(z)
    return np.array(x_rk4), np.array(y_rk4), np.array(z_rk4)

def plot_rk4(x_rk4, y_rk4, z_rk4):
    plt.figure(figsize=(10, 6))
    plt.plot(x_rk4, y_rk4, marker='o', label='RK4 y-values', color='blue')
    plt.plot(x_rk4, z_rk4, marker='o', label='RK4 z-values', color='black')
    plt.title('Runge-Kutta 4th Order Method by Abisekh Pandey')
    plt.xlabel('x')
    plt.ylabel('y and z')
    plt.legend()
    plt.grid()
    plt.show()

x0 = 0
y0 = 1
z0 = 1
xn = 1
h = 0.05

x_rk4, y_rk4, z_rk4 = rk4(x0, y0, z0, xn, h)
plot_rk4(x_rk4, y_rk4, z_rk4)
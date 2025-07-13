import numpy as np
import matplotlib.pyplot as plt

def cubicSpline(x, y, value):
    n = len(x)
    for i in range(n):
        if value == x[i]:
            return y[i]
    h = np.diff(x)

    A = np.zeros((n, n))
    B = np.zeros(n)

    A[0, 0] = 1
    A[n-1, n-1] = 1

    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        B[i] = 6 * ((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])

    M = np.linalg.solve(A, B)
    
    i = np.searchsorted(x, value) - 1

    return (M[i+1]/(6*h[i]) * (value - x[i])**3 - M[i]/(6*h[i])*(value - x[i+1])**3 + (y[i+1]/h[i] - M[i+1]*h[i]/6)*(value - x[i]) - (y[i]/h[i] - M[i]*h[i]/6)*(value - x[i+1]))

def plotCubicSpline(x, y, x_value):
    plt.scatter(x, y, marker='o', color="#000000", label="Data Points")
    x_curve = np.linspace(x[0], x[-1], 1000)
    y_curve = [cubicSpline(x, y, i) for i in x_curve]
    plt.plot(x_curve, y_curve, color="coral", label ="Cubic Spline Curve")
    plt.plot(x_value, cubicSpline(x,y, x_value), color="#ff0000", label = 'Result', marker='x')
    plt.title("Cubic Spline Curve Interpolation by Abisekh Pandey")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.savefig("Images/cubic_spline3.png")
    plt.show()

# Generate 13 random (x, y) pairs, sort by x, and assign to x and y
points = np.random.uniform([[0, 0]], [[20, 30]], (13, 2))
points = points[points[:, 0].argsort()]
x = points[:, 0]
y = points[:, 1]
x_value = 10.5
plotCubicSpline(x, y, x_value)
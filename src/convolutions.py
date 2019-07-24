
import numpy as np
import matplotlib.pyplot as plt


def show_plot(title, data, kernel):
    print(title)
    print(data * kernel)

    plt.title(title + ", conv=" + str((data * kernel).sum()))
    plt.imshow(data, cmap='GnBu')
    plt.show()


im_v = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

k_v = np.array([
    [-1, 1, -1],
    [-1, 1, -1],
    [-1, 1, -1]
])

show_plot("Vertical line", im_v, k_v)

im_h = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
])

k_h = np.array([
    [-1, -1, -1],
    [1, 1, 1],
    [-1, -1, -1]
])

show_plot("Horizontal line", im_h, k_h)

im_p = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

k_p = np.array([
    [-1, -1, -1],
    [-1, 1, -1],
    [-1, -1, -1]
])

show_plot("Spot", im_p, k_p)


im_dp = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

k_dp = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, 1]
])

show_plot("Dark Spot", im_dp, k_dp)

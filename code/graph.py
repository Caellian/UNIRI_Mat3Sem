#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

def f():
    return 2*X**3 + 2*Y**3 - 36*X*Y + 430

def f_der_x():
    return 6*X**2 - 36*Y

def f_der_y():
    return 6*Y**2 - 36*X

def save_figure(of, path, z_label='z', font_size='medium', angle=[-60, 30]):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(azim=angle[0], elev=angle[1])

    ax.plot_surface(X, Y, of)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel(z_label, fontsize=font_size)

    plt.savefig(path)

save_figure(f(), 'figures/graf_f.png', z_label='$f(x, y)$', angle=[-70, 30])
save_figure(f_der_x(), 'figures/graf_fdx.png', z_label='$\\frac{\\partial f}{\\partial x}$', font_size='xx-large', angle=[60, 30])
save_figure(f_der_y(), 'figures/graf_fdy.png', z_label='$\\frac{\\partial f}{\\partial y}$', font_size='xx-large', angle=[60, 30])

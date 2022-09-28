import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def func(cord1, cord2, visual = 'all'):
    a = cord2[1] - cord1[1]
    b = cord1[0] - cord2[0]
    c = a * cord1[0] + b * cord1[1]

    if visual == 'show':
        plt.plot(cord1, cord2)
        plt.plot(cord1, cord2, 'o')
        plt.show()
    elif visual == 'print':
        if b < 0:
            print(f'{a}*x{b}*y={c}')
        else:
            print(f'{a}*x+{b}*y={c}')
    elif visual == 'all':
        if b < 0:
            print(f'{a}*x{b}*y={c}')
        else:
            print(f'{a}*x+{b}*y={c}')

        plt.plot(cord1, cord2)
        plt.plot(cord1, cord2, 'o')
        plt.show()


func(np.array([3, 2]), np.array([5, 7]), 'all')
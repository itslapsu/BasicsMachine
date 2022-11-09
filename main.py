import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

N=50
x = np.linspace(0, 1, num=N)
t = np.sin(2 * np.pi * x)
t1 = t + 0.2 * np.random.randn(N)


plt.plot(x, t)
plt.plot(x, t, 'ro')
plt.show()

plt.plot(x, t1)
plt.plot(x, t1, 'ro')
plt.show()

pred = np.poly1d(np.polyfit(x, t1, 3))

plt.plot(x, pred(x))
plt.plot(x, t1, 'ro')
plt.show()
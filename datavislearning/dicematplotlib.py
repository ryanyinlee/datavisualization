import matplotlib.pyplot as plt
import numpy as np
from dice import Die

plt.style.use('_mpl-gallery')

die0 = Die()

x = range(10)
y = [die0.roll() for value in range(10)]

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 10), xticks=np.arange(1, 8),
ylim=(0, 14), yticks=np.arange(1, 8))

plt.show()
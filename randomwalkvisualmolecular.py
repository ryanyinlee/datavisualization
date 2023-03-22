import matplotlib.pyplot as plt

#from randomwalk import RandomWalk
from randomwalkmod import RandomWalk

rw = RandomWalk()
rw.create_walks()

plt.style.use('classic')

fig, ax = plt.subplots(figsize=(14,8), dpi = 128)

point_nums = range(rw.numpoints)

ax.plot(rw.xvals, rw.yvals, linewidth = 1)

ax.scatter(0, 0, c='green', edgecolors='none', s=50)
ax.scatter(rw.xvals[-1], rw.yvals[-1], c='red', edgecolors='none', s=50)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
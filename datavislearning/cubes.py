import matplotlib.pyplot as plt

xvals = range(1,5001)
yvals = [x**3 for x in xvals]

fig, ax = plt.subplots()

ax.scatter(xvals, yvals, c=yvals, cmap = plt.cm.Reds, s=10)
ax.ticklabel_format(useOffset=False, style='plain')

plt.show()
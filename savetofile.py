import matplotlib.pyplot as plt

xvals = range(1,1001)

yvals = [x**2 for x in xvals]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(xvals,yvals, c='red',s=10)

ax.set_title('square nums', fontsize = 24)
ax.set_xlabel('value', fontsize = 14)
ax.set_ylabel('square of value', fontsize = 14)

ax.tick_params(axis = 'both', which='major', labelsize = 14)

ax.axis([0, 1100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')
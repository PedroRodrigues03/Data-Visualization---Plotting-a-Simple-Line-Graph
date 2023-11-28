import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)

ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cube Values', fontsize=14)

ax.axis([0, 1100, 0, 1100000000])

plt.savefig('cube_plot.png', bbox_inches='tight')
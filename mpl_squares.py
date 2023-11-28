import matplotlib.pyplot as plt

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

# The plt.style.use() method allows me to change the background color to the chart
plt.style.use('seaborn-v0_8-darkgrid')

"""
The variable fig represents the entire figure or collection of plots that are generated.
The variable ax represents a single plot in the figure and is the variable i'll use most of the time
"""
fig, ax = plt.subplots()

# The scatter() method allows me to plot a series of points passing first the values of xlabel then ylabel
ax.scatter(input_values, squares, s=10)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

# Set the size of tick labels
ax.tick_params(axis="both", labelsize=10)

plt.savefig("squares_plot.png", bbox_inches='tight')
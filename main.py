from matplotlib.pyplot import plot, xlabel, ylabel, title, legend, show
from numpy import linspace
from xymethod import random_x_y

coordinates = random_x_y(1, 20)

x = linspace(0, coordinates[0], 100)
y = linspace(0, coordinates[1], 100)

plot(x, y, label='linear')
xlabel('x label')
ylabel('y label')
title('Simple Plot')
legend()
show()
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'b-', linewidth=2.0, label='Linear')
plt.plot(t, t**2, 'r--', linewidth=2.0, label='Quadratic')
plt.plot(t, t**3, 'g^', linewidth=2.0, label='Cubic')

plt.xlabel('Dummy data for X-axis')
plt.ylabel('Dummy data for Y-axis')
plt.legend(['Linear', 'Quadratic', 'Cubic'], loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
plt.title('An example of a graph')
plt.annotate('Divergence point', xy=(1.4, 3), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.savefig('graph.png')
plt.show()

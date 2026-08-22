import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2*np.pi, 500)
r = 5
plt.plot(r*np.cos(t), r*np.sin(t))
plt.scatter([0],[0],color='red')
plt.title('Circle primitive'); plt.axis('equal'); plt.grid(True); plt.show()

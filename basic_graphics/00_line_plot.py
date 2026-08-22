import matplotlib.pyplot as plt

x = list(range(11))
y = [2*i + 1 for i in x]
plt.plot(x, y, marker='o')
plt.title('Line primitive')
plt.xlabel('x'); plt.ylabel('y')
plt.grid(True); plt.axis('equal'); plt.show()

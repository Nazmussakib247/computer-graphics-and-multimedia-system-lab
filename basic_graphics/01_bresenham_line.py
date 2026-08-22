import matplotlib.pyplot as plt

x0, y0, x1, y1 = 2, 1, 15, 9
points=[]
dx, dy = abs(x1-x0), abs(y1-y0)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1
err = dx - dy
while True:
    points.append((x0,y0))
    if x0 == x1 and y0 == y1: break
    e2 = 2*err
    if e2 > -dy: err -= dy; x0 += sx
    if e2 < dx: err += dx; y0 += sy
px, py = zip(*points)
plt.scatter(px,py,s=80); plt.plot(px,py,alpha=.4)
plt.title('Integer line points'); plt.grid(True); plt.axis('equal'); plt.show()

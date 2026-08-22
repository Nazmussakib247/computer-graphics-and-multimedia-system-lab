import random
import matplotlib.pyplot as plt
vertices=[(0,0),(1,0),(0.5,0.866)]
x,y=0.2,0.2; xs=[]; ys=[]
for _ in range(20000):
    vx,vy=random.choice(vertices); x=(x+vx)/2; y=(y+vy)/2; xs.append(x); ys.append(y)
plt.scatter(xs,ys,s=.2); plt.title('Sierpinski triangle'); plt.axis('equal'); plt.axis('off'); plt.show()

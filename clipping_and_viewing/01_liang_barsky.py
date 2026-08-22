import matplotlib.pyplot as plt
box=(0,10,0,8); p1=(-4,7); p2=(14,1)
# Parameter sampling shows the segment retained inside the clipping window.
pts=[]
for i in range(1001):
    t=i/1000; x=p1[0]+t*(p2[0]-p1[0]); y=p1[1]+t*(p2[1]-p1[1])
    if box[0]<=x<=box[1] and box[2]<=y<=box[3]: pts.append((x,y))
plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'--',label='input')
if pts: x,y=zip(*pts); plt.plot(x,y,linewidth=4,label='clipped')
plt.legend(); plt.grid(); plt.axis('equal'); plt.show()

import matplotlib.pyplot as plt
window=(0,10,0,8)
line=(-4,2,14,7)
x0,y0,x1,y1=line
# Simple sampling view of accepted points for an easy visual lab.
xs=[]; ys=[]
for t in [i/500 for i in range(501)]:
    x=x0+t*(x1-x0); y=y0+t*(y1-y0)
    if window[0]<=x<=window[1] and window[2]<=y<=window[3]: xs.append(x); ys.append(y)
plt.plot([x0,x1],[y0,y1],'--',label='input'); plt.plot(xs,ys,linewidth=4,label='visible part')
plt.xlim(-5,15); plt.ylim(-2,10); plt.legend(); plt.grid(); plt.show()

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
img=Image.new('RGB',(240,160),'white'); d=ImageDraw.Draw(img)
d.rectangle((30,30,210,130),fill=(30,120,220)); d.ellipse((80,45,160,125),fill=(240,180,40))
rot=img.rotate(20,expand=True)
plt.subplot(1,2,1); plt.imshow(img); plt.axis('off'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(rot); plt.axis('off'); plt.title('Rotated'); plt.show()

##  UTILIZANDO MATPLOTLIB   ##

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#img = cv2.imread('lobo.jpg', 0)
#plt.hist(img.ravel(),256,[0,256])
#plt.show())

#img = cv2.imread('a0004.jpg')
#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()

##  UTILIZANDO OPENCV   ##

#CREAR MASCARA PRIMERO
img = cv2.imread('lobo.jpg')
mask = np.zeros(img.shape [:2],np.uint8)
mask[10:250, 100:250] = 255
masked_img =cv2.bitwise_and(img,img,mask = mask)

#CALCULAR EL HISTOGRAMA CON MÁSCARA Y SIN MASCARA
#FIJAR EL TERCER ARGUMENTO COMO "MASK"
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(221), plt.imshow(img,'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img,'gray')
plt.subplot(224), plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
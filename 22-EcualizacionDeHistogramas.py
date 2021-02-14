import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)

#Genera el histograma de la imagen
hist, bins = np.histogram(img.flatten(), 256,[0,256])

#Genera la funcion de distribucion acumulada (cdf por sus siglas en ingles )
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

#genera los gráficos del histograma y de la funcion de distribucion acumulada 
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256],color = 'r')
plt.xlim([0,256])
plt.legend(('cdf', 'histograma'), loc = 'upper right')
plt.show()
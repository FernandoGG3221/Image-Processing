import cv2
import numpy as np 

img= cv2.imread('lobo.jpg',0)
equ= cv2.equalizeHist(img)
res = np.hstack((img,equ)) #Agrupa las imagenes una al lado de la otra
cv2.imshow('lob',res)
cv2.waitKey(0)
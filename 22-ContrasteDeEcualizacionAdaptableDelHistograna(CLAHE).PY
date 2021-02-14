import cv2 
import numpy as np 

img = cv2.imread('lobo.jpg',0)

#Crea un objeto de CLAHE (los argumentos son opcionales)
clahe= cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.namedWindow('imagen',cv2.WINDOW_NORMAL)
cv2.imshow('imagen',cl1)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindow()
#Contador monedas

from cv2 import cv2
#Imagen original
imagen=cv2.imread("Monedascontorno/contorno.jpg")
#Imagen en grises
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#Imagen en umbral
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

contorno, jerarquia= cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1, (51,60,251), 2)

#Mostrar imagen
cv2.imshow('imagen original',imagen)
#cv2.imshow('imagen',grises)
#cv2.imshow('Imagen umbral',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()




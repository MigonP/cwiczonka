import cv2
import numpy as np
#czytanie img
img= cv2.imread('circles.jpg')
#konwersia Brg Hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#gama kolorow jakie ma wyszikiwac
lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
#okienka
cv2.imshow("Image", img)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
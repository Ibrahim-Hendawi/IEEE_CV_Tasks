import cv2
import numpy as np

# Read the image
img = cv2.imread('1.jpg')
img = cv2.resize(img,(300, 400))
# desplay the original Image
cv2.imshow('Original', img)

# increse britness 
iImg = cv2.add(img, (100, 100, 100 ,0))
cv2.imshow('increased', iImg)

# decrease britness
dImg = cv2.subtract(img, (100,100,100,0))
cv2.imshow('decreased', dImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
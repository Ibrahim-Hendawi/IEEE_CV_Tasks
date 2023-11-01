import numpy as np
import cv2

img = cv2.imread('010.jpg')


rimg = cv2.resize(img, (256,256))

cv2.imwrite('resized_image.jpg',rimg)


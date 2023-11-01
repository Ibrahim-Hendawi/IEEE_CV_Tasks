import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    # press esc key to exit form loop
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
import cv2
# import time
# import numpy as np
# import math
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    cv2.imshow("Img", img)
    lm = detector.findPosition(img)
    r = 0.0
    try:
        if ((((lm[4][1]-lm[8][1])**2)+((lm[4][2]-lm[8][2])**2))**0.5)/240 > 1:
            r = 1
        else:
            r = ((((lm[4][1]-lm[8][1])**2)+((lm[4][2]-lm[8][2])**2))**0.5)/240
        print(r)
    except:
        print("NO HAND VISIBLE")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

import cv2
# import time
# import numpy as np
# import math
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.7)

last_angle = None
last_length = None

minAngle = 0
maxAngle = 180
angle = 0
angleBar = 400
angleDeg = 0
minHand = 50  # 50
maxHand = 300  # 300
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

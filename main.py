import cv2
import mouse
import wx
# import time
# import numpy as np
# import math
import HandTrackingModule as htm

app = wx.App(False)
width, height = wx.GetDisplaySize()

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.7)
i = 0
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    cv2.imshow("Img", img)
    i += 1
    if i == 2:  # Adding stability to cursor position
        lm = detector.findPosition(img)
        r = 0.0
        try:
            mouse.move(lm[8][1] * 2, lm[8][2] * 2)
            print(((((lm[4][1] - lm[8][1]) ** 2) + ((lm[4][2] - lm[8][2]) ** 2)) ** 0.5) / 240)
            if ((((lm[4][1] - lm[8][1]) ** 2) + ((lm[4][2] - lm[8][2]) ** 2)) ** 0.5) / 240 < 0.1:
                mouse.click()
        except:
            print("NO HAND VISIBLE")
        finally:
            i = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

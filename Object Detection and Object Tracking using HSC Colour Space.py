#HSV = Hue Saturation Value
#Hue = 0 - 360 | Color Component (Base Pigment)
#Saturation = 0 - 100% | Amount or Depth of Colour
#Value = 0 - 100% | Brightness of color

import cv2
import numpy as np

def nothing(x): #Dummy Function
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)   #LowerHue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)   #LowerSaturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)   #LowerValue
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # frame = cv2.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\six-coloured-balls.jpg')
    # frame = cv2.resize(frame, (300, 300))

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v]) #LowerBlue
    u_b = np.array([u_h, u_s, u_v]) #UpperBlue

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    #Set LH = 110, LS = 50, LV = 50, UH = 130, US = 255, UV = 255 TO SEE ONLY BLUE COLOUR IN THE IMAGE
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()




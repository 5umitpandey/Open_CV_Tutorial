import numpy as np
import cv2

#Drawing a black image using np
#img = np.zeros([900, 900, 3], np.uint8)

img = cv2.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\coalminestrip.jpeg', 1)

#Drawing line on image (name_of_img, (x,y), (x1,y1), (b,g,r), thickness)
img = cv2.line(img, (0,0), (255,255), (0,0,255), 10)

#Drawing arrowed line
img = cv2.arrowedLine(img, (0,285), (255,285), (255,0,0), 10)

#Drawing Rectangle
"""
x1,y1--------
|           |
|           |
|           |
--------x2,y2
"""
#img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 10)

#Filling rectangle with colour provided (thickness = -1)
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), -1)

#Drawing Circle
#( img, (x,y), (radius), (bgr), (thickness or -1) )
img = cv2.circle(img, (600,200), 63, (255, 255, 0), -1)

#Text on Image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (300, 800), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

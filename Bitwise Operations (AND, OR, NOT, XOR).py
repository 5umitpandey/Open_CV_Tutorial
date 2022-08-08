#Uncomment lines to see the output

import cv2
import numpy as np

#Creating black image
img1 = np.zeros((250, 500, 3), np.uint8)

#Inserting rectangle
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)

#Creating another image of white colour
img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

#Performing Bitwise operations on img1 and img2
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
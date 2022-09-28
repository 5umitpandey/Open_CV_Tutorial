import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\coalminestrip.jpeg', -1)
cv.imshow('image', img)

plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

#Link to run this on Google Colab in case it does'nt work on your computer
r'https://colab.research.google.com/drive/1Nv4fSuqTXCZc3vyJWbAPoLXWAZ21LP2P?usp=sharing'
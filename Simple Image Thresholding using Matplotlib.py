import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'D:\gnimmargorP\Python\Open_CV_Tutorial\bw_gradient.jpg', 0)
img = cv.resize(img, (750, 550))

#In Adaptive Thresholding we focus on particular areas of an image to get more detail.
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Orignal Image', 'Binary', 'Binary_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
 
plt.show()

#Link to run this on Google Colab in case it doesn't work on your computer
r'https://colab.research.google.com/drive/1BMl6KNvtOtEbpCg0x5MQwQ3QUUoG8bgl?usp=sharing'
#Morphological Transformations are normally performed on binary images.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'D:\gnimmargorP\Python\Open_CV_Tutorial\six-coloured-balls.jpg', 0)
img = cv.resize(img, (750, 550))

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

#change the values of 5,5 to see the changes
kernel = np.ones( (5, 5), np.uint8)
dilation = cv.dilate(mask, kernel, iterations = 2)
erosion = cv.erode(mask, kernel, iterations=2)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = ['Image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
 
plt.show()

#Link to run this on Google Colab in case it doesn't work on your computer
r'https://colab.research.google.com/drive/1vUWEsZp9VahmLE43EUcjH59eda8VGVuH?usp=sharing'
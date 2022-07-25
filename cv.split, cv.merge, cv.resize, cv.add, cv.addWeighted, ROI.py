import cv2
import numpy as np

img = cv2.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\Messi_Image_With_Ball.jpg')

print(img.shape)    #returns a tuple of rows, columns, and channels
print(img.size)     #returns Total no of pixels 
print(img.dtype)    #returns image's datatype

b, g, r = cv2.split(img)
img = cv2.merge( (b, g, r) )

#Work required on the below code
# ROI = Region Of Interest
#Target the ball's coordinate and copy it to another source
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

#Add two images
img2 = cv2.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\Transparent_image.png')

#Resizing both the images to same size
img = cv2.resize(img, (300, 300))
img2 = cv2.resize(img2, (300, 300))

#dst = cv2.add(img, img2) #add function

#Adding two images with weights ( sum of the weights should be = 1)
dst = cv2.addWeighted(img, .6, img2, .4, 0) #add function

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
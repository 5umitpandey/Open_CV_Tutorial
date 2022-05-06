import cv2

#reading image (-1, 0, 1) are colours of image
img = cv2.imread('D:\gnimmargorP\Python\Open_CV_Tutorial\coalminestrip.jpeg',-1)

#printing image in matrix form
# print(img)

#opening image
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    #writing image
    cv2.imwrite('D:\gnimmargorP\Python\Open_CV_Tutorial\img_copy1.jpeg', img)
    cv2.destroyAllWindows()
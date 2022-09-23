import cv2 as cv
import numpy as np


img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow('blank', blank)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blurred = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)


# canny = cv.Canny(blurred, 125, 175)
# cv.imshow('edge', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # binarizing the image
cv.imshow('thres', thresh)

# 443 contours using threshold method

contours, hierarachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}, contour(s) found!')

cv.drawContours(blank,contours, -1, (0,0,255), 2)
cv.imshow('drawn', blank)

# 687 contours for canny immage with approx_simple and with none
# 26 contours with blurred

cv.waitKey(0)
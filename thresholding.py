import cv2 as cv

img = cv.imread('photos/catt.jfif')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding

threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)

# adaptive thresholding - better

adap = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('adaptive threshold', adap)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.jpg") #stores the image in as 'img' from the path

cv.imshow("cat", img)             #displays the image in a new window (window name first arg)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian - not much used

lap = cv.Laplacian(gray,cv.CV_64F)
lap= np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel - more used in advanced computing

sobelx = cv.Sobel(gray,cv.CV_64F, 1,0)
sobely = cv.Sobel(gray,cv.CV_64F, 0,1)
com_sobel = cv.bitwise_or(sobelx,sobely) 

cv.imshow('sobelx',sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined sobel', com_sobel)

# canny

canny = cv.Canny(gray,150,255)
cv.imshow('canny', canny)



cv.waitKey(0)
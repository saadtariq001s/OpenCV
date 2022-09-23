
import numpy as np
import cv2 as cv  

img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

#gray = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)
#cv.imshow('B/W', gray)
 
# graycale image
img2 = cv.imread('photos/cat.jpg',0)
cv.imshow('cat grey', img2)

# blurring

blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascading

cany = cv.Canny(img, 125,175 )
cv.imshow('edges', cany)


# dilating the image - on cascaded imgaes only

dilated= cv.dilate(cany, (3,3), iterations=3)
cv.imshow('dilated', dilated)

# eroded - reverrt back from dilated to cascaded

eroded = cv.erode(dilated, (3,3), iterations=7)
cv.imshow('erode', eroded)

# resizing the image

resized = cv.resize(img, (1500,1100), interpolation= cv.INTER_CUBIC)  
# interpolation = INTER AREA FOR SMALLER IMAGES, INTERCUBIC OR INTERLINEAR FOR BIGGER
cv.imshow('resized', resized)

# cropping

cropped = img[50:200, 400:500]
cv.imshow('crop', cropped)
cv.waitKey(0)
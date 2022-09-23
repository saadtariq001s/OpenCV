import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype= 'uint8')  

# uint8 is the datatype of an image
# if we're to color it, we need to enter the color channels as the third parameter in np.zeros

cv.imshow('blank', blank)



blank2 = np.zeros((500,500, 3), dtype= 'uint8')  

# uint8 is the datatype of an image
# if we're to color it, we need to enter the color channels as the third parameter in np.zeros

blank2[:] = 0,0,255                  # for all pixels color red
cv.imshow('Green', blank2)

blank2[200:300, 300:400] = 255,0,0   # paint only a portion of pixels
cv.imshow('abcdsd', blank2)

# drawing a rectangle

cv.rectangle(blank2, (0,0), (250,500), (0,255,0), thickness=-1)

# thickness= -1 / FILLED for colored rect, any int for not colored

cv.imshow('rect', blank2)

# drawing a circle

cv.circle(blank, (250,250), 50, (255,255,0), thickness=-1)
cv.imshow('crc', blank)

# drawing a line

cv.line(blank, (0,0), (250,300), (255,0,0), thickness=2)
cv.imshow('line', blank )

# adding text to an image

blank3 = np.zeros((500,500,3), dtype= 'uint8')

cv.putText(blank3, "Hello World", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,255), 2)
cv.imshow('text', blank3)



cv.waitKey(0)

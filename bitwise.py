import cv2 as cv
import numpy as np

blank = np.zeros((600,600), dtype='uint8')

rec = cv.rectangle(blank.copy(), (50,50),(500,500),255,-1)
cir = cv.circle(blank.copy(), (300,300), 200, 255,-1)

cv.imshow('circle', cir)
cv.imshow('rectangle', rec)

# Bitwise_AND 

bitwise_and = cv.bitwise_and(rec,cir)
cv.imshow('bit AND', bitwise_and)

# Bitwise_OR

bitwise_or = cv.bitwise_or(rec,cir)
cv.imshow('bit OR', bitwise_or)

# Bitwise_XOR

bitwise_xor = cv.bitwise_xor(rec,cir)
cv.imshow('bit xor', bitwise_xor)

# Bitwise_NOT

bitwise_not = cv.bitwise_not(rec,cir)
cv.imshow('bit not', bitwise_not)

cv.waitKey(0)


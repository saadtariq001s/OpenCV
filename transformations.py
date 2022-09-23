import cv2 as cv
import numpy as np

img = cv.imread('photos/abc.jpg')
cv.imshow('cat', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)


    # -x = left
    # +x = right
    # -y = up
    # y = down


translated = translate(img, 50, 100)
cv.imshow('translation', translated)


# rotation

def rotate(img, angle, rotPoint= None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)    

rotated = rotate(img, 45)    
cv.imshow('rotated', rotated)

# flipping

flip = cv.flip(img, -1)
cv.imshow('flip', flip)

# 0 = flip horizontal
# 1 = flip verical
# -1 = both


### Cropping again

cropped = img[0:100, 200:300]
cv.imshow('cropped', cropped)

cv.waitKey(0)
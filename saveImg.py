import cv2 as cv
import numpy as np

img = cv.imread("photos/pen.jfif",0)

print(type(img))

cv.imwrite("photos/abc.jpg",img)
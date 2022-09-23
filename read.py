import cv2 as cv

img = cv.imread("photos/cat_large.webp")

cv.imshow("cat_larger", img)

cv.waitKey(0)

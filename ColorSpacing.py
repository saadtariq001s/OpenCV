import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

# BGR to RGB 
# default color coding of opencv is BGR, and matplotlib is RGB, hence colors get inverted 

imgg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(imgg)


# BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR TO HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('la', hsv)

plt.show()
cv.waitKey(0)
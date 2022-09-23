import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray,gray, mask= circle)
cv.imshow('masked', masked)

#gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256])

plt.figure()
plt.title('Coloured Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
#plt.xlim([0,256])
#plt.plot(gray_hist)


colors = ('b', 'g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],masked,[256],[0,256])
    plt.plot(hist,color= col)
    plt.xlim([0,256])
plt.show()





cv.waitKey(0)
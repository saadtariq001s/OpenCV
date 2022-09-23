import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cats', img)

# blurring or smoothing

# Method 1 - Averaging
# Creates a kernel of a given size, moves around pic, takes average of the surrounding pixels and use it to blur the center pixel

average = cv.blur(img, (7,7))
cv.imshow('blurr avg', average)


# Method 2 -- Gaussian Blurr
# Similar to average but more realistic, blurs lesser, assigns weight to the surrounding pixels then take avg

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('guass blur', gauss)

# Method 3 -- Median BLur

med = cv.medianBlur(img, 7)  # used for realtime/professional CV projects
cv.imshow('medBlur', med)

# Method 4 -- Bilateral (Best as they say)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)




cv.waitKey(0)

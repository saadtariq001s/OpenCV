import cv2 as cv

from rescale_video import rescaleFrame

img = cv.imread("photos/cat.jpg")     # image loads and stores in img
cv.imshow("Cat", img)

def rescaleImg(img, scale=0.75):
    w = int(img.shape[1] * scale)
    h = int(img.shape[0] * scale)

    dimensions = (w,h)

    return cv.resize(img ,dimensions)

#resized_image = rescaleFrame(img)
#cv.imshow("img" ,resized_image)

resized_img = rescaleImg(img)
cv.imshow("img",resized_img)
cv.destroyAllWindows ()                             # destroy all windows

cv.waitKey(0)


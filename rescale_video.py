# rescaling/resizing is done to reduce computational strain
# resizing height and width

import cv2 as cv

img = cv.imread("photos/cat.jpg")     # image loads and stores in img
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):        # defining a function for rescaling, taking frame as an 
                                            # input paramter, default scale being 0.75      
    width = int(frame.shape[1] * scale)     # shape[1] indicates width
    height = int(frame.shape[0] * scale)    # shape [0 indicates height]
    
    dimensions = (width, height)            # creates tuple of width and height

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # resampling using pixel area relation  

resized_image = rescaleFrame(img)
cv.imshow("Image", resized_image)

capture = cv.VideoCapture("videos/football.mp4")        # frame by frame captures the video from the path

while True :                                  
    isTrue , frame = capture.read ()              # make sure if every frame is read

    frame_resize = rescaleFrame(frame, scale=0.2)
     
    cv.imshow ('Video' , frame)                 # show each frame in a seperate window
    cv.imshow('Video Resized', frame_resize)
    if cv.waitKey ( 20 ) & 0xFF == ord ('d'):   # run it until alphabet 'd' is entered and stop the video
     break
capture.release ()                                 # release the capture contents
cv.destroyAllWindows ()                             # destroy all windows



cv.waitKey(0)
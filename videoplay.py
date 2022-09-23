import cv2 as cv

capture = cv.VideoCapture("videos/football.mp4")        # frame by frame captures the video from the path

while True :                                  
    isTrue , frame = capture.read ()               # make sure if every frame is read 
    cv.imshow ('Video' , frame)                 # show each frame in a seperate window
    if cv.waitKey ( 20 ) & 0xFF == ord ('d'):   # run it until alphabet 'd' is entered and stop the video
     break
capture.release ()                                 # release the capture contents
cv.destroyAllWindows ()                             # destroy all windows

# -215 assertion error = opencv couldnt find more frames and ran out of frames, closing unexpectedly
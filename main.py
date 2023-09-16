<<<<<<< HEAD
import cv2 as cv
import numpy as np
from src.lib.posture_recognition import get_basic_contours

import cv2 # See video 1 for installation
import numpy as np

# Replace "0" with a file path to work with a saved video
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

num_frames = stream.get(cv2.CAP_PROP_FRAME_COUNT)
frame_ids = np.random.uniform(size=20) * num_frames
frames = []
for fid in frame_ids:
    stream.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("SOMETHING WENT WRONG")
        exit()
    frames.append(frame)

# The median frame here is our background
median = np.median(frames, axis=0).astype(np.uint8)
median = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))



stream.set(cv2.CAP_PROP_POS_FRAMES, 0)
while True:
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("No more stream :(")
        break
    
    # take out any pixel that is similar to our median frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dif_frame = cv2.absdiff(median, frame)
    threshold, diff = cv2.threshold(dif_frame, 100, 255,
                    cv2.THRESH_BINARY)
    # frame = cv2.resize(frame, (width, height))

    cv2.imshow("Video!", cv2.blur(diff, (10,10)))
    cv2.waitKey(5)
    if cv2.waitKey(1) == ord('q'): # press "q" to quit
        break

stream.release()
cv2.destroyAllWindows() #!

=======

import cv2 as cv2

# from src.lib.posture_recognition import get_basic_contours3


cap = cv2.VideoCapture(0)

if not cap.isOpened():
 print("Cannot open camera")
 exit()
while True:
 # read frame1, resize and convert to grayscale
    ret, frame1 = cap.read()
    if frame1 is None:
        break
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # read frame2, resize and convert to grayscale
    ret2, frame2 = cap.read()
    if frame2 is None:
        break
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # compute the difference between frames
    diff = cv2.absdiff(gray1, gray2)
    # blur image
    blurred = cv2.GaussianBlur(diff, (11, 11), 0)

    # global thresholding
    ret3, th1 = cv2.threshold(blurred, 85, 255, cv2.THRESH_BINARY)
    #print(th1.dtype)

    cnts = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # other way to find contours = same error
    # hierarchy, contours = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('dist', frame1)
    cv2.imshow('thresh', th1)
    cv2.imshow('blurred', blurred)

    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



#  # Capture frame-by-frame
#  ret, frame = cap.read()
#  # if frame is read correctly ret is True
#  if not ret:
#     print("Can't receive frame (stream end?). Exiting ...")
#     break
#  #contours = get_basic_contours3(frame)

#  #finds countrs within frame and draws contour (source image, contours passed as list, index of contours -1 for all, colour, thickness)
#  #frame = cv.drawContours(frame, contours, -1, (0,255,0)) 
#  #frame = get_basic_contours3(frame)


 
#  frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#  # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
#  contours, hierarchy = cv.findContours(image=frame, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
                                      
#  # draw contours on the original image
#  image_copy = frame.copy()
#  cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)
                
#  # see the results
#  cv.imshow('None approximation', image_copy) 

#  # Display the resulting frame
#  # cv.imshow('frame', frame)
 
>>>>>>> d495eda24311a2e53db0599f6b0cf836e04083fc

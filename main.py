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


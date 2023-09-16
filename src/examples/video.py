
import cv2 as cv

from lib.posture_recognition import get_basic_contours


cap = cv.VideoCapture(0)
if not cap.isOpened():
 print("Cannot open camera")
 exit()
while True:
 # Capture frame-by-frame
 ret, frame = cap.read()
 # if frame is read correctly ret is True
 if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
 contours = get_basic_contours(frame)
 frame = cv.drawContours(frame, contours, -1, (0,255,0))
 # Display the resulting frame
 cv.imshow('frame', frame)
 if cv.waitKey(1) == ord('q'):
    break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
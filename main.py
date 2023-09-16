import cv2
import time
from src.lib.posture_recognition import get_contour_mask, is_slouching 
print("Getting proper posture...")
proper_mask = get_contour_mask() 
camera = cv2.VideoCapture(0)
time.sleep(5)

current_posture_mask = get_contour_mask()

print(is_slouching(proper_mask, current_posture_mask, 100))






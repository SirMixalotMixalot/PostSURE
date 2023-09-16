import time
from src.lib.posture_recognition import get_contour_mask, is_slouching 
print("Getting proper posture...")
proper_mask = get_contour_mask() 
time.sleep(1)

current_posture_mask = get_contour_mask()

print("You are slouching!" if is_slouching(proper_mask, current_posture_mask, 6/100) else "You aren't slouching")






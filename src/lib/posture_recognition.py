import numpy as np
import cv2
import matplotlib.pyplot as plt

import torch
from torchvision.models.segmentation import deeplabv3_resnet101
from torchvision import transforms

import numpy as np
 

def get_contour_mask():
    def make_deeplab(device):
        deeplab = deeplabv3_resnet101(pretrained=True).to(device)
        deeplab.eval()
        return deeplab

    device = torch.device("cpu")
    deeplab = make_deeplab(device)

    camera = cv2.VideoCapture(0)
    _, image = camera.read()

<<<<<<< HEAD
    k = min(1.0, 1024/max(image.shape[0], image.shape[1]))
    image = cv2.resize(image, None, fx=k, fy=k, interpolation=cv2.INTER_LANCZOS4)

    deeplab_preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    def apply_deeplab(deeplab, img, device):
        input_tensor = deeplab_preprocess(img)
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = deeplab(input_batch.to(device))['out'][0]
        output_predictions = output.argmax(0).cpu().numpy()
        return (output_predictions == 15)
    mask = apply_deeplab(deeplab, image, device)

    return mask
=======
    # find the contours from the thresholded image
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours



def get_basic_contours3(myimage):
    # BG Remover 3
    myimage_hsv = cv2.cvtColor(myimage, cv2.COLOR_BGR2HSV)
     
    #Take S and remove any value that is less than half
    s = myimage_hsv[:,:,1]
    s = np.where(s < 127, 0, 1) # Any value below 127 will be excluded
 
    # We increase the brightness of the image and then mod by 255
    v = (myimage_hsv[:,:,2] + 127) % 255
    v = np.where(v > 127, 1, 0)  # Any value above 127 will be part of our mask
 
    # Combine our two masks based on S and V into a single "Foreground"
    foreground = np.where(s+v > 0, 1, 0).astype(np.uint8)  #Casting back into 8bit integer
 
    background = np.where(foreground==0,255,0).astype(np.uint8) # Invert foreground to get background in uint8
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)  # Convert background back into BGR space
    foreground=cv2.bitwise_and(myimage,myimage,mask=foreground) # Apply our foreground map to original image
    finalimage = background+foreground # Combine foreground and background
 
    return finalimage
>>>>>>> d495eda24311a2e53db0599f6b0cf836e04083fc

import numpy as np
import cv2
import matplotlib.pyplot as plt

import torch
from torchvision.models.segmentation import deeplabv3_resnet101, DeepLabV3_ResNet101_Weights
from torchvision import transforms

import numpy as np

PERSON = 15

def get_contour_mask():
    def make_deeplab(device):
        deeplab = deeplabv3_resnet101(weights=DeepLabV3_ResNet101_Weights.DEFAULT).to(device)
        deeplab.eval()
        return deeplab

    device = torch.device("cpu")
    deeplab = make_deeplab(device)

    camera = cv2.VideoCapture(0)
    _, image = camera.read()

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
        return (output_predictions == PERSON)
    mask = apply_deeplab(deeplab, image, device)
    
    return mask

                            

def is_slouching(mask_proper_posture, mask,threshold) -> bool:
    wrong_doings = 0
    total_pixels = mask.shape[0] * mask.shape[1]
    for (p1,p2) in zip(mask_proper_posture.flatten(), mask.flatten()):
        wrong_doings += abs(int(p1) - int(p2))
    print(wrong_doings)
    print(total_pixels)
    return (wrong_doings/total_pixels) > threshold
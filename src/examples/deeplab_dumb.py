import numpy as np
import cv2
import matplotlib.pyplot as plt

import torch
from torchvision.models.segmentation import deeplabv3_resnet101
from torchvision import transforms

def make_deeplab(device):
    deeplab = deeplabv3_resnet101(weights=True).to(device)
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
    return (output_predictions == 15)
mask = apply_deeplab(deeplab, image, device)

print(mask)
print(mask.shape)
plt.imshow(mask, cmap="gray")
plt.show()



# function to identify top of head to shoulder distance
# get output for when slouching, when straight (and store to database later)

# def left_head_to_shoulder(mask): 
#     def find_top_x_y(mask):
#             for y in range(mask.shape[0]): 
#                  for x in range(mask.shape[1]):
#                     if mask[y][x]:
#                          return (x,y)
    
#     delta_x = 10
#     gradients = {}
#     top_ys = {}
#     top_x = find_top_x_y(mask)[0]
#     top_y = find_top_x_y(mask)[1]

#     for x in range(top_x, 10, -10):
#         x1 = x-10 # right x
#         x2 = x # left x 
#         # find difference in highest y at x1 and x2
#         def find_top_y(mask, x):
#              for y in range(mask.shape[0]):
#                   if mask[y][x]:
#                        top_ys[x] = y
#                        return y
#         y1 = find_top_y(mask, x1)
#         y2 = find_top_y(mask, x2)
#         dy = abs(y1-y2)
#         gradients[x1] = dy
    
#     # find x when dy is greatest --> get average y values AFTER largest drop --> set as shoulder height
#     x_at_max_dy = max(gradients, key=gradients.get)
#     shoulder_y_avg = 0
#     for x in range(x_at_max_dy-20, x_at_max_dy+10, 10): 
#          shoulder_y_avg += top_ys.get(x)
#     shoulder_y_avg = shoulder_y_avg/3 

#     head_to_shoulder = top_y - shoulder_y_avg
#     return head_to_shoulder




         

#def is_slouching(mask, )
from PIL import ImageGrab
import numpy as np
import cv2
import win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

print(width, height)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height,))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Capture', img_final)
    cv2.waitKey(10)

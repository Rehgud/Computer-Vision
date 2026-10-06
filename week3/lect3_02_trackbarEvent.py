import cv2
import numpy as np

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소 값:", add_value)

    image = image + add_value
    cv2.imshow(title, image)

image = np.zeros((480, 640), np.uint8)
title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

cv2.waitKey(0)
cv2.destoryAllWindows()
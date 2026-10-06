import cv2
import numpy as np

image = np.zeros((480, 640), np.uint8)
image[:] = 128

title = "Position"

cv2.namedWindow(title)

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destoryAllWindows()
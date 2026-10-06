import cv2
import numpy as np

image = np.zeros((480, 640), np.uint8)
image[:] = 200

title1, title2 = 'Position1', 'Position2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150) # 원점(display 왼쪽 상단 기준)에서 x로 150, y로 150
cv2.moveWindow(title2, 400, 50) # 원점에서 x로 400, y로 50에 위치

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destoryAllWindows()
import cv2
import numpy as np

image = np.zeros((240, 320), np.uint8)
image[:] = 255

title1, title2 = 'Autosize', 'Normal'

# 행렬 크기 변경없이 윈도우 크기 변경
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) 
# 행렬 크기 변경되어 보여지며 윈도우 크기 변경, 실제 행렬이 변경되는 것은 아님
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)

cv2.waitKey(0)
cv2.destoryAllWindows()
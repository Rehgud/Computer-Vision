import cv2
import numpy as np

image = np.zeros((240, 320), np.uint8)
image[:] = 0 # 검은색

title1, title2, title3 = 'Window1', 'Window2', 'Window3'

cv2.namedWindow(title1)
cv2.namedWindow(title2)
cv2.namedWindow(title3)

cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, 320, 0)
cv2.moveWindow(title3, 0, 270)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.imshow(title3, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
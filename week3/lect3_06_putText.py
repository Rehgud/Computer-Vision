import cv2
import numpy as np

# 세리프체가 기본임

image = np.zeros((250, 500, 3), np.uint8)
image[:] = (255, 255, 255)

pt1 = (50, 200)
pt2 = (50, 260)

cv2.putText(image, 'SIMPLEX', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (42, 42, 165)) # brown
cv2.putText(image, 'DUMPLEX', (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 3, (128, 128, 0)) # olive
cv2.putText(image, 'TRIPLEX', pt1, cv2.FONT_HERSHEY_SIMPLEX, 2, (221, 160, 221)) # violet
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image, 'ITALIC', pt2, fontFace, 4, (211, 160, 221)) # violet

cv2.imshow("Put Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
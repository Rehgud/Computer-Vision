import cv2
import numpy as np

image = np.zeros((350, 500, 3), np.uint8)
image[:] = (255, 255, 255)

pt1 = (300, 50)
pt2 = (100, 220)

center = (image.shape[1] // 2, image.shape[0] // 2)
shade = (pt2[0] + 2, pt2[1] + 2)

cv2.circle(image, center, 100, (255, 0, 0))
cv2.circle(image, pt1, 50, (0, 165, 255))
cv2.circle(image, pt2, 70, (255, 255, 0), -1) # fill

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, 'center_blue', center, font, 1.0, (255, 0, 0))
cv2.putText(image, 'pt1_orange', pt1, font, 0.8, (0, 165, 255))
cv2.putText(image, 'pt2_cyan', shade, font, 1.2, (0, 0, 0))
cv2.putText(image, 'pt2_cyan', pt2, font, 1.2, (255, 255, 0), 1)

cv2.imshow("Draw circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

switch_case = {
    ord('c'): 'c키 입력',
    ord('d'): 'd키 입력',
    ord('C'): 'C키 입력',
    ord('D'): 'D키 입력'
}

image = np.zeros((480, 640), dtype=np.uint8)

cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)
    if key == ord('q'):
        break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
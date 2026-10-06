import numpy as np
import cv2

switch_case = {
    ord('a'): 'a키 입력',
    ord('b'): 'b키 입력',
    0x41: 'A키 입력',
    int('0x42', 16): "B키 입력",
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image = np.zeros((480, 640), np.uint8)

cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100) # 화살표키 등 특수키 인지 위해 사용 = waitKeyEx
    if key == 27:
        break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
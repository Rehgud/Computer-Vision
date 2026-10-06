import numpy as np
import cv2

def onChange(value):
    global image, title
    image[:] = value
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if image[0][0] < 246:
            image = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    if event == cv2.EVENT_LBUTTONDOWN:
        if image[0][0] >= 10:
            image = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

image = np.zeros((480, 640), np.uint8)

title = "Trackbar & Mouse Event"
bar_name = 'brightness'

cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)

while True:
    key = cv2.waitKeyEx(100)

    if key == 2555904:                      # 오른쪽 화살표
        if image[0][0] < 246:
            image = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    elif key == 2424832:                    # 왼쪽 화살표
        if image[0][0] >= 10:
            image = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    elif key == ord('q') or key == ord('Q'):  # 종료
        break

cv2.destroyAllWindows()
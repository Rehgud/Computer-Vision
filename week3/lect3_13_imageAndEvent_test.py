import cv2

title = 'imageK'
image = cv2.imread("read_color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("read Error")

def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 5, (0, 0, 255), 2)
        cv2.putText(image, str(image[y, x]), (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        cv2.imshow(title, image)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
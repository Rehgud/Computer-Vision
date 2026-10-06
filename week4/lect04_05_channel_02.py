import cv2

image = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("Unable to open image file.")

bgr = cv2.split(image)
cv2.add(bgr[0], 100, bgr[0])
merge_bgr = cv2.merge(bgr)
print("bgr data type:", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr element size:", len(bgr))

cv2.imshow("image", image)
cv2.imshow("Blue channel", bgr[0])
cv2.imshow("Green channel", bgr[1])
cv2.imshow("Red channel", bgr[2])
cv2.imshow("merge_bgr", merge_bgr)

cv2.waitKey(0)
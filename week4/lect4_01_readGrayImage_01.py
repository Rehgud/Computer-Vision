import cv2

def print_matInfo(name, image):
    if image.dtype == 'uint8':   mat_type = "CV_8U"
    elif image.dtype == 'int8':  mat_type = "CV_8S"
    elif image.dtype == 'uint16': mat_type = "CV_16U"
    elif image.dtype == 'int16': mat_type = "CV_16S"
    elif image.dtype == 'float32': mat_type = "CV_32F"
    elif image.dtype == 'float64': mat_type = "CV_64F"
    else: mat_type = str(image.dtype)

    nchannel = 3 if image.ndim == 3 else 1

    print("%12s: shape =%s, dtype = %s, depth = %s, channels = %d"
          % (name, image.shape, image.dtype, mat_type, nchannel))

title1 = 'gray2gray'
title2 = 'gray2color'

gray2gray = cv2.imread("read_gray.jpg", cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread("read_gray.jpg", cv2.IMREAD_COLOR)

if gray2gray is None or gray2color is None:
    raise Exception("read Error")

print("Pixel value: [100, 100]")
print("Title1: ", gray2gray[100, 100])
print("Title2: ", gray2color[100, 100])

print_matInfo(title1, gray2gray)
print_matInfo(title2, gray2color)

cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)
cv2.destroyAllWindows()
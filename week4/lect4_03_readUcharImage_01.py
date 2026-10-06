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

title1 = '16bit unchanged'
title2 = '32bit unchanged'

color2unchanged1 = cv2.imread("read_16.tif", cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("read_32.tif", cv2.IMREAD_UNCHANGED)

if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("read Error")

print("pixel value : [10, 10]")
print(title1, ":", type(color2unchanged1[10][10][0]), color2unchanged1[10, 10])
print(title2, ":", type(color2unchanged2[10][10][0]), color2unchanged2[10, 10])

print_matInfo(title1, color2unchanged1)
print_matInfo(title2, color2unchanged2)

cv2.imshow(title1, color2unchanged1)
cv2.imshow(title2, color2unchanged2)
cv2.waitKey(0)
cv2.destroyAllWindows()
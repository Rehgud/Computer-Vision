import numpy as np
import cv2

ch0 = np.zeros((2, 4), np.uint8) + 10
ch1 = np.zeros((2, 4), np.uint8) + 20
ch2 = np.zeros((2, 4), np.uint8) + 30

list_bgr = [ch0, ch1, ch2]
merge_bgr = cv2.merge(list_bgr)
split_bgr = cv2.split(merge_bgr)

print("split_bgr Array shape:", np.array(split_bgr).shape)
print("merge_bgr Array shape:", merge_bgr.shape)
print("[ch0] = \n%s" % ch0)
print("[ch1] = \n%s" % ch1)
print("[ch2] = \n%s" % ch2)
print("[merge_bgr] = \n%s \n" % merge_bgr)

print("[split_bgr[0]] = \n%s" % split_bgr[0])
print("[split_bgr[1]] = \n%s" % split_bgr[1])
print("[split_bgr[2]] = \n%s" % split_bgr[2])
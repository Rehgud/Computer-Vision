import cv2

capture = cv2.VideoCapture("video_file2.avi")

if not capture.isOpened(): raise Exception("Unable to open video")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)

# frame_rate: 초당 프레임 수
# delay: 프레임 시간
# width: 너비
# height: 높이
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resolution: ", width, 'x', height)
print("Frame rate: ", frame_rate)
print("Delay: ", delay)
frame_cnt = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = capture.read()

    if not ret or cv2.waitKey(delay) >= 0:
        break

    # frame number 출력
    frame_cnt += 1
    cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
    cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (255, 255, 0), 3)
    cv2.imshow("Video file", frame)

capture.release()
cv2.destroyAllWindows()
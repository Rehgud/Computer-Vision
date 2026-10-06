import cv2

capture = cv2.VideoCapture("video_file2.avi")
if not capture.isOpened(): raise Exception("Unable to open video file.")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt = 0
font = cv2.FONT_HERSHEY_SIMPLEX

fourcc = cv2.VideoWriter_fourcc(*'FMP4')
writer = cv2.VideoWriter("video_file2_out.mp4", fourcc, frame_rate, (width, height))

while True:
    ret, frame = capture.read()

    if not ret or cv2.waitKey(delay) >= 0:
        break
    bgr = cv2.split(frame)
    frame_cnt += 1

    if frame_cnt > 90:
        break
    elif frame_cnt <= 30:
        cv2.subtract(bgr[1], 255, bgr[1])   # 파란 화면: G, R 제거
        cv2.subtract(bgr[2], 255, bgr[2])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)      # 그림자
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (0, 0, 255), 3)    # 빨간 글씨
    elif frame_cnt <= 60:
        cv2.subtract(bgr[0], 255, bgr[0])   # 녹색 화면: B, R 제거
        cv2.subtract(bgr[2], 255, bgr[2])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (255, 0, 0), 3)    # 파란 글씨
    elif frame_cnt <= 90:
        cv2.subtract(bgr[0], 255, bgr[0])   # 빨간 화면: B, G 제거
        cv2.subtract(bgr[1], 255, bgr[1])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (0, 255, 0), 3)    # 녹색 글씨

    writer.write(frame)
    cv2.imshow("Video file", frame)

capture.release()
writer.release()
cv2.destroyAllWindows()
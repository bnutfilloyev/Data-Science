import cv2
import numpy as np

height = 1024
width = 600
x1, y1, x2 = 0, 0, 600
line = 0


cap = cv2.VideoCapture(0)
# face_image = cv2.imread('face.png')
# accept_image = cv2.imread('accept.png')
# reject_image = cv2.imread('reject.png')


def resize_frame(frame):
    frame = cv2.resize(frame, (640*1024//480, 1024))

    frame = frame[:, frame.shape[1]//2 - 300: frame.shape[1] // 2 + 300]

    return frame


def line_down_frame(image, line):

    if line >= height * 2:
        line = 0

    line += 50
    temp_line = line
    result = frame

    for alpha in range(50, 100, 1):
        cv2.line(image, (0, temp_line//2), (width, temp_line//2),
                 (36, 255, 12), thickness=2, lineType=8)
        temp_line -= 10

        result = cv2.addWeighted(image, 1-alpha/100, result, alpha/100, 0)


    return result, line


while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = resize_frame(frame)
    image = frame.copy()

    # image = cv2.addWeighted(frame, 1, face_image, 1, 0)

    result, line = line_down_frame(image, line)

    # alpha = 50
    # result = accept_image
    # result = cv2.addWeighted(image, 1, accept_image, 1, 0)
    # cv2.putText(result, 'Nutfilloyev Bexruz', (150, 700), cv2.FONT_HERSHEY_SIMPLEX,
    #             1, (36, 255, 12), thickness=2, lineType=8)

    # result = cv2.addWeighted(image, 1, reject_image, 1, 0)
    # cv2.putText(result, 'Reject', (700, 500), cv2.FONT_HERSHEY_SIMPLEX,
    #             1, (36, 255, 12), thickness=2, lineType=8)




    cv2.imshow('frame', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

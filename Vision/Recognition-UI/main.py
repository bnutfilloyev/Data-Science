import cv2
import numpy as np

height = 1024
width = 600

cap = cv2.VideoCapture(0)


def resize_frame(frame):
    frame = cv2.resize(frame, (640*1024//480, 1024))

    frame = frame[:,frame.shape[1]//2 - 300: frame.shape[1] // 2 + 300]

    return frame

def line_down_frame(image):
    if line >= height *2:
        line = 0
    line += 50
    temp_line = line
    result = frame
    
    for alpha in range(50, 100, 1):
        cv2.line(image, (0, temp_line//2),(width, temp_line//2), (36, 255, 12), thickness=2, lineType=8)
        temp_line -= 10

        result = cv2.addWeighted(image, 1-alpha/100, result, alpha/100, 0)
    return result


x1, y1, x2 = 0, 0, 600
line = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = resize_frame(frame)
    image = frame.copy()
    
    result = line_down_frame(image)
    
    cv2.imshow('frame', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


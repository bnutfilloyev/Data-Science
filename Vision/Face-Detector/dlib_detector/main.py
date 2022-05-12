import os

import cv2
import dlib

detector = dlib.get_frontal_face_detector()

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "images")

images = os.listdir(image_path)

count = 0
for image in images:
    img = cv2.imread(os.path.join(image_path, image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    print("IMAGE: ", image)

    if len(faces) < 1:
        count += 1
    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y


print("[INFO] {} images have no faces".format(count))
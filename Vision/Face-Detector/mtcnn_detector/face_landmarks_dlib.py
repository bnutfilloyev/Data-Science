import os

import cv2
import dlib
from mtcnn import MTCNN
from imutils import face_utils

detector = MTCNN()

base_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(base_path, 'models')
predictor_path = os.path.join(model_path, 'shape_predictor_68_face_landmarks.dat')
predictor = dlib.shape_predictor(predictor_path)

images_path = os.path.join(base_path, 'images')
images = os.listdir(images_path)

for image in images:
    img = cv2.imread(os.path.join(images_path, image))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detect_faces(img)
    print(faces)
    for face in faces:
        x, y, w, h = face['box']
        shape = predictor(img_gray, dlib.rectangle(x, y, x + w, y + h))
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
    cv2.imshow('img', img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

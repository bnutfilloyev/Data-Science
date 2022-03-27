#!/usr/bin/env python

import cv2
import numpy as np
import os
import insightface
from insightface.app import FaceAnalysis
from tqdm import tqdm
from time import time
from PIL import Image, ImageOps
from scipy.spatial.distance import cosine

height = 1024
width = 600
x1, y1, x2 = 0, 0, 600
known_people_list = []


# face_image = cv2.imread('face.png')
# accept_image = cv2.imread('accept.png')
# reject_image = cv2.imread('reject.png')

def load_known_faces():
    known_faces = "me/"
    list_images = os.listdir(known_faces)
    for img_name in tqdm(list_images):
        person_name = img_name.split(".")[0]
        image_path = os.path.join(known_faces, img_name)
        image = cv2.imread(image_path)
        face_encodings = app.get(image)
        if len(face_encodings) == 0:
            print("Cannot extract face feature from : {}".format(img_name))
            continue
        person = {}
        person["name"] = person_name
        person["embedding"] = face_encodings[0].embedding
        known_people_list.append(person)


def key_func(person):
    return person["sim"]


def resize_frame(frame):
    frame = cv2.resize(frame, (640*1024//480, 1024))

    frame = frame[:, frame.shape[1]//2 - 300: frame.shape[1] // 2 + 300]

    return frame


def line_down_frame(image, line):

    if line >= height * 2:
        line = 0

    line += 50
    temp_line = line
    result = image

    for alpha in range(50, 100, 1):
        cv2.line(image, (0, temp_line//2), (width, temp_line//2),
                 (36, 255, 12), thickness=2, lineType=8)
        temp_line -= 10

        result = cv2.addWeighted(image, 1-alpha/100, result, alpha/100, 0)

    return result, line


def find_face(embedding):
    best_matches = []

    for person in known_people_list:
        sim = 1 - cosine(person["embedding"], embedding)
        if(sim > 0.5):
            known = {}
            known["person"] = person
            known["sim"] = sim
            best_matches.append(known)
    if len(best_matches) == 0:
        return
    best_matches.sort(key=key_func)
    return best_matches[0]


def main():

    load_known_faces()
    cap = cv2.VideoCapture(-1)
    line = 0

    while(1):

        _, frame = cap.read()

        cv2.namedWindow('img', cv2.WINDOW_FREERATIO)
        cv2.setWindowProperty(
            'img', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # print(_)

        result = resize_frame(frame)

        faces = app.get(frame)

        for face in faces:
            # print(face)
            bbox = face.bbox
            x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
            cv2.rectangle(frame, (int(x1), int(y1)),
                          (int(x2), int(y2)), (0, 255, 0), 1)
            person = find_face(face.embedding)

            if person is None:
                continue

            print("recognized as: {}, similarity: {}".format(
                person["person"]["name"], person["sim"]))

        result, line = line_down_frame(result, line)

        cv2.imshow("img", result)

        k = cv2.waitKey(10)
        if k == ord("q"):
            cv2.destroyAllWindows()
            # cap.release()
            break


# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break


#     frame = resize_frame(frame)
#     image = frame.copy()

#     # image = cv2.addWeighted(frame, 1, face_image, 1, 0)

#     result, line = line_down_frame(image, line)

#     # alpha = 50
#     # result = accept_image
#     # result = cv2.addWeighted(image, 1, accept_image, 1, 0)
#     # cv2.putText(result, 'Nutfilloyev Bexruz', (150, 700), cv2.FONT_HERSHEY_SIMPLEX,
#     #             1, (36, 255, 12), thickness=2, lineType=8)

#     # result = cv2.addWeighted(image, 1, reject_image, 1, 0)
#     # cv2.putText(result, 'Reject', (700, 500), cv2.FONT_HERSHEY_SIMPLEX,
#     #             1, (36, 255, 12), thickness=2, lineType=8)


#     cv2.imshow('frame', result)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


if __name__ == '__main__':
    app = FaceAnalysis(name='buffalo_s', providers=[
                       'CUDAExecutionProvider', 'CPUExecutionProvider'], allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))

    main()
    # img = ins_get_image('test')
    # faces = app.get(img)
    # for face in faces:
    #     print(face)

import os

import cv2
from mtcnn import MTCNN

detector = MTCNN()

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, 'images/')

images = os.listdir(image_path)

count = 0
for image in images:
    img = cv2.imread(os.path.join(image_path, image))
    result = detector.detect_faces(img)
    print("Image: {}".format(image))
    # print(result)
    print(result[0]['box'])
    print("\n")
    if len(result) < 1:
        count += 1

print("Number of images with no faces detected: {}".format(count))
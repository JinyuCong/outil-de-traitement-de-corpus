from deepface import DeepFace
import cv2
import os
import glob

images_path = "../data/raw/happy"
save_path = "../data/cleaned/happy"

n = 0

for img in glob.glob(os.path.join(images_path, "*.jpg")):
    try:
        face_objs = DeepFace.extract_faces(
            img_path=img,
            target_size=(224,224),
            detector_backend='opencv',
            enforce_detection=False,
            grayscale=True
        )
        face = face_objs[0]['face'] * 255
        cv2.imwrite(os.path.join(save_path, f"happy{n}.jpg"), face)
        print(f"image {n} saved")
        n += 1
    except ValueError:
        continue

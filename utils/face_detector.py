"""
Face detection using OpenCV's built-in Haar Cascade classifier.

This runs independently of the MobileNetV2 object classifier, since
ImageNet (the dataset MobileNetV2 is trained on) has no "person" or
"face" class - it's built for objects, not people. Running dedicated
face detection alongside it means the app correctly recognizes when
a human is in frame instead of guessing an unrelated object.
"""

import cv2
import numpy as np

# Haar Cascade XML files ship with opencv-python - no separate download needed
_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
_face_cascade = cv2.CascadeClassifier(_cascade_path)


def detect_faces(filepath: str):
    """
    Detects human faces in the image.
    Returns a list of bounding boxes as (x, y, w, h) tuples.

    Parameters are tuned to be conservative (higher minNeighbors,
    larger minSize) to reduce false positives on animal faces,
    which can otherwise trigger the cascade due to similar
    round/symmetric facial patterns.
    """
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError("Could not read image file for face detection.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    img_h, img_w = gray.shape[:2]
    min_dim = int(min(img_h, img_w) * 0.12)  # face must be a reasonable fraction of the image

    faces = _face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=10,
        minSize=(max(60, min_dim), max(60, min_dim)),
    )

    return [tuple(map(int, face)) for face in faces]


def draw_face_boxes(filepath: str, faces, output_path: str):
    """
    Draws bounding boxes around detected faces and saves the
    annotated image to output_path.
    """
    image = cv2.imread(filepath)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (110, 255, 143), 3)

    cv2.imwrite(output_path, image)

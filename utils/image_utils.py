"""
Image preprocessing utilities using OpenCV.
Handles reading, resizing, and preparing uploaded images for the model.
"""

import cv2
import numpy as np


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(filepath: str, target_size=(224, 224)):
    """
    Reads an image from disk with OpenCV, converts BGR -> RGB,
    resizes to the model's expected input size, and returns both:
    - the preprocessed array (for the model)
    - the original image dimensions (for UI display)
    """
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError("Could not read image file. It may be corrupted or an unsupported format.")

    original_h, original_w = image.shape[:2]

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(image_rgb, target_size, interpolation=cv2.INTER_AREA)

    array = np.expand_dims(resized.astype(np.float32), axis=0)

    return array, (original_w, original_h)

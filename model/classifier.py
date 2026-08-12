"""
Image classifier powered by a pretrained MobileNetV2 (ImageNet weights).
MobileNetV2 is small and fast enough to run comfortably on CPU, which
makes it a good fit for a lightweight web demo, while still recognizing
1000 real-world object classes out of the box.
"""

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions,
)

from utils.image_utils import preprocess_image


class ImageClassifier:
    def __init__(self):
        # include_top=True keeps the final classification layer (1000 ImageNet classes)
        self.model = MobileNetV2(weights="imagenet", include_top=True)

    def predict(self, filepath: str, top_k: int = 3):
        """
        Returns a list of {label, confidence} dicts for the top_k predictions,
        plus the original image dimensions.
        """
        image_array, original_size = preprocess_image(filepath, target_size=(224, 224))
        processed = preprocess_input(image_array)

        raw_predictions = self.model.predict(processed, verbose=0)
        decoded = decode_predictions(raw_predictions, top=top_k)[0]

        results = [
            {
                "label": label.replace("_", " ").title(),
                "confidence": round(float(score) * 100, 2),
            }
            for (_, label, score) in decoded
        ]

        return results, original_size


# Singleton - model loads once at startup, not per-request
classifier = ImageClassifier()

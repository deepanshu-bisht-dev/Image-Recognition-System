"""
Image Recognition System - Flask app.
Upload an image, get real-time predictions from a pretrained
MobileNetV2 model (1000 ImageNet classes).
"""

import os
import uuid
from flask import Flask, render_template, request, jsonify, url_for

from utils.image_utils import allowed_file
from utils.face_detector import detect_faces, draw_face_boxes
from model.classifier import classifier

# Common substrings covering ImageNet's ~120 dog breeds + other animal classes.
# Used to suppress a Haar Cascade false-positive "face" when the object
# classifier is already confident the subject is an animal, not a person.
_ANIMAL_KEYWORDS = [
    "dog", "poodle", "retriever", "terrier", "hound", "spaniel", "shepherd",
    "collie", "bulldog", "mastiff", "pug", "chihuahua", "husky", "corgi",
    "dachshund", "beagle", "pointer", "setter", "schnauzer", "cat", "kitten",
    "tabby", "persian cat", "siamese", "bird", "parrot", "wolf", "fox",
    "bear", "lion", "tiger", "horse", "cow", "ox", "sheep", "ram", "pig",
    "elephant", "monkey", "ape", "gorilla", "chimpanzee", "snake", "lizard",
    "fish", "shark", "whale", "rabbit", "hare", "deer", "goat", "camel",
    "kangaroo", "panda", "raccoon", "squirrel", "otter", "seal",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type. Use PNG, JPG, JPEG, or WEBP."}), 400

    ext = file.filename.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
    file.save(filepath)

    try:
        faces = detect_faces(filepath)
        predictions, original_size = classifier.predict(filepath, top_k=3)
    except Exception as e:
        return jsonify({"error": f"Could not process image: {str(e)}"}), 500

    # If the classifier is confident the subject is an animal, treat any
    # detected "face" as a false positive (common with Haar Cascade on
    # round/furry animal faces) and suppress it.
    top_label = predictions[0]["label"].lower() if predictions else ""
    top_confidence = predictions[0]["confidence"] if predictions else 0
    is_confident_animal = top_confidence >= 25 and any(kw in top_label for kw in _ANIMAL_KEYWORDS)

    if is_confident_animal:
        faces = []

    display_filename = unique_name

    if faces:
        # Draw bounding boxes and save an annotated version for display
        annotated_name = f"annotated_{unique_name}"
        annotated_path = os.path.join(app.config["UPLOAD_FOLDER"], annotated_name)
        draw_face_boxes(filepath, faces, annotated_path)
        display_filename = annotated_name

        face_count = len(faces)
        face_label = "Human Face Detected" if face_count == 1 else f"{face_count} Human Faces Detected"
        predictions = [{"label": face_label, "confidence": 98.0}] + predictions

    return jsonify({
        "predictions": predictions,
        "faces_detected": len(faces),
        "image_url": url_for("static", filename=f"uploads/{display_filename}"),
        "original_size": {"width": original_size[0], "height": original_size[1]},
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

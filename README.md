# 👁️ VISION — Real-Time Image Recognition System

An AI-powered web app that classifies objects in any uploaded image in real time,
using a pretrained deep learning model. Built as part of my Python Developer
Internship at **Codec Technologies**.

## 🚀 Features

- **Real-time classification** — upload any image and get predictions in under a second
- **Top-3 predictions with confidence scores** — not just one guess, a ranked breakdown
- **1000 object classes** — powered by MobileNetV2 trained on ImageNet
- **Human face detection** — a dedicated OpenCV Haar Cascade pipeline detects and highlights
  faces with a bounding box, since the object classifier alone isn't trained to recognize people
- **OpenCV preprocessing pipeline** — proper image decoding, color conversion, and resizing
- **Distinctive "machine vision" UI** — drag-and-drop scanner with animated scan-line and
  reticle overlay, built from scratch (no UI framework)

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|---------------------------------------|
| Backend        | Python, Flask                        |
| Model          | TensorFlow / Keras (MobileNetV2, ImageNet weights) |
| Image Processing | OpenCV                             |
| Frontend       | HTML, CSS, JavaScript (vanilla)      |

## 📂 Project Structure

```
image-recognition-app/
├── app.py                   # Flask app & prediction API
├── model/
│   └── classifier.py         # MobileNetV2 loading + inference
├── utils/
│   ├── image_utils.py         # OpenCV preprocessing
│   └── face_detector.py       # OpenCV Haar Cascade face detection
├── templates/index.html      # Scanner UI
├── static/css/style.css      # Machine-vision styling
├── static/js/upload.js       # Drag-drop, preview, results rendering
├── requirements.txt
└── README.md
```

## ⚙️ Running Locally

```bash
# Clone the repo
git clone https://github.com/deepanshu-bisht-dev/image-recognition-system.git
cd image-recognition-system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://localhost:5001` in your browser. The MobileNetV2 weights (~14MB)
download automatically on first run.

## 📌 How It Works

1. User drags/drops or selects an image in the scanner UI
2. Image is sent to `/api/predict` as multipart form data
3. OpenCV runs Haar Cascade face detection on the image first
4. In parallel, OpenCV converts BGR → RGB and resizes the image to 224×224 for the classifier
5. MobileNetV2 (pretrained on ImageNet) runs inference on the preprocessed array
6. If faces were detected, bounding boxes are drawn on the image and a "Human Face Detected"
   result is added to the top of the results list
7. Top predictions with confidence scores are returned and rendered with animated confidence bars

## 📈 Future Improvements

- Fine-tune on a custom dataset for domain-specific classification
- Webcam-based live classification
- Batch upload support

---

Built by [Deepanshu Bisht](https://github.com/deepanshu-bisht-dev) as part of the Python Developer Internship at Codec Technologies.

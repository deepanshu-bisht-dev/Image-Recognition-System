<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=220&section=header&text=VISION&fontSize=70&fontColor=00F5D4&fontAlignY=38&desc=Real-Time%20AI%20Image%20Recognition%20System&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2500&pause=800&color=00F5D4&center=true&vCenter=true&width=650&lines=Upload+any+image+%E2%80%94+get+predictions+in+%3C1+second;Powered+by+MobileNetV2+%2B+OpenCV;1000+object+classes+%7C+Real-time+face+detection;Built+during+my+Python+Developer+Internship" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-MobileNetV2-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

[![Stars](https://img.shields.io/github/stars/deepanshu-bisht-dev/Image-Recognition-System?style=for-the-badge&color=00F5D4&labelColor=1a1a1a)](https://github.com/deepanshu-bisht-dev/Image-Recognition-System/stargazers)
[![Forks](https://img.shields.io/github/forks/deepanshu-bisht-dev/Image-Recognition-System?style=for-the-badge&color=00F5D4&labelColor=1a1a1a)](https://github.com/deepanshu-bisht-dev/Image-Recognition-System/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/deepanshu-bisht-dev/Image-Recognition-System?style=for-the-badge&color=00F5D4&labelColor=1a1a1a)](https://github.com/deepanshu-bisht-dev/Image-Recognition-System/commits/main)

**⭐ If this project catches your eye, drop it a star — it genuinely helps! ⭐**

</div>

<br/>

## 👁️ What is VISION?

**VISION** is an AI-powered web app that identifies what's inside any image — in real time. Drop in a photo, and within a second it classifies the object across **1,000 categories**, detects human faces with bounding boxes, and shows a **ranked, confidence-scored breakdown** — all wrapped in a custom-built, machine-vision-themed scanner UI (no UI framework, built from scratch).

Built during my **Python Developer Internship at Codec Technologies.**

<br/>

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎬 Demo](#-demo)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [📌 How It Works](#-how-it-works)
- [📈 Roadmap](#-roadmap)
- [🤝 Connect](#-connect)

<br/>

## ✨ Features

| | |
|---|---|
| ⚡ **Real-time classification** | Upload any image, get predictions in under a second |
| 🏆 **Top-3 ranked predictions** | Not just one guess — a full confidence-scored breakdown |
| 🧠 **1000 object classes** | Powered by MobileNetV2 trained on ImageNet |
| 🙂 **Human face detection** | Dedicated OpenCV Haar Cascade pipeline draws bounding boxes around faces |
| 🎨 **Custom machine-vision UI** | Drag-and-drop scanner with animated scan-line + reticle overlay, built from scratch |
| 🔧 **Robust CV pipeline** | Proper decoding, BGR→RGB conversion, and resizing before inference |

<br/>

## 🎬 Demo

> 📸 **Add your own screenshots here.** Create an `assets/` folder in the repo, drop in 2-3 screenshots (upload screen, scan animation, results panel), then reference them like this:
> ```markdown
> <img src="assets/demo.png" width="85%"/>
> ```
> This renders 100% reliably since the image lives inside your own repo — no third-party service involved.

<br/>

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</div>

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Model** | TensorFlow / Keras — MobileNetV2 (ImageNet weights) |
| **Image Processing** | OpenCV (preprocessing + Haar Cascade face detection) |
| **Frontend** | HTML, CSS, vanilla JavaScript — no framework |

<br/>

## 📂 Project Structure

```
image-recognition-app/
├── app.py                    # Flask app & prediction API
├── model/
│   └── classifier.py          # MobileNetV2 loading + inference
├── utils/
│   ├── image_utils.py          # OpenCV preprocessing
│   └── face_detector.py        # OpenCV Haar Cascade face detection
├── templates/
│   └── index.html              # Scanner UI
├── static/
│   ├── css/style.css           # Machine-vision styling
│   └── js/upload.js            # Drag-drop, preview, results rendering
├── requirements.txt
└── README.md
```

<br/>

## ⚙️ Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/deepanshu-bisht-dev/Image-Recognition-System.git
cd Image-Recognition-System

# 2. Create a virtual environment (Python 3.12 recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **`http://localhost:5001`** in your browser. MobileNetV2 weights (~14MB) download automatically on first run.

<br/>

## 📌 How It Works

```mermaid
flowchart LR
    A[📤 User uploads image] --> B[Flask receives file<br/>at /api/predict]
    B --> C[OpenCV: Haar Cascade<br/>face detection]
    B --> D[OpenCV: BGR→RGB +<br/>resize to 224×224]
    D --> E[MobileNetV2 inference<br/>ImageNet weights]
    C --> F[Draw bounding boxes<br/>if faces found]
    E --> G[Top-3 predictions +<br/>confidence scores]
    F --> H[🖥️ Render results in<br/>scanner UI]
    G --> H
```

1. User drags/drops or selects an image in the scanner UI
2. Image is sent to `/api/predict` as multipart form data
3. OpenCV runs Haar Cascade face detection on the image
4. In parallel, OpenCV converts BGR → RGB and resizes the image to 224×224
5. MobileNetV2 (pretrained on ImageNet) runs inference on the preprocessed array
6. If faces are detected, bounding boxes are drawn and a "Human Face Detected" result is added to the top
7. Top predictions with confidence scores render as animated confidence bars

<br/>

## 📈 Roadmap

- [ ] Fine-tune on a custom dataset for domain-specific classification
- [ ] Webcam-based live classification
- [ ] Batch upload support
- [ ] Deploy a live demo link

<br/>

## 🤝 Connect

<div align="center">

Built by **Deepanshu Bisht** as part of the Python Developer Internship at Codec Technologies.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/deepanshu-bisht-853731379)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepanshu-bisht-dev)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/deepanshu___25/)

**If VISION impressed you, a ⭐ on this repo goes a long way — thank you!**

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=100&section=footer" width="100%"/>

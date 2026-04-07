# ♻️ Plastic Object Detection using YOLO & Streamlit

A real-time and image-based **Plastic Object Detection System** built using **YOLO (Ultralytics)** and **Streamlit**.  
This application detects plastic objects from uploaded images as well as through a **live webcam feed**, helping support environmental monitoring and waste management initiatives.

---

## 🚀 Features

- 📷 **Image Upload Detection**
  - Upload JPG, JPEG, or PNG images
  - Automatic plastic object detection with bounding boxes

- 🎥 **Real-Time Webcam Detection**
  - Live plastic detection using your system camera
  - Adjustable confidence threshold

- ⚙️ **Customizable Confidence Threshold**
  - Control detection sensitivity from the sidebar

- 🎨 **Modern UI**
  - Dark-themed Streamlit interface
  - Clean layout and responsive design

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – Frontend web interface
- **YOLO (Ultralytics)** – Object detection model
- **OpenCV** – Webcam and image processing
- **NumPy**
- **Pillow (PIL)**

---

## 📂 Project Structure

```

├── app.py                  # Main Streamlit application
├── best.pt                 # Trained YOLO model (not included in repo)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/plastic-object-detection.git
cd plastic-object-detection
````

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add YOLO Model

Place your trained YOLO model file in the project root:

```text
best.pt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🖥️ How It Works

1. Select detection mode from the sidebar:

   * **Image Upload**
   * **Real-Time Webcam**
2. Adjust the confidence threshold
3. View detected plastic objects with bounding boxes and labels

---

## 🌍 Use Cases

* Environmental monitoring
* Smart waste management systems
* Recycling automation
* Research & academic projects
* AI-powered sustainability solutions

---

## ⚠️ Notes

* Ensure your webcam is accessible for real-time mode
* `best.pt` must be compatible with Ultralytics YOLO
* GPU is recommended for better performance (optional)

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this software.

---

## 👤 Authors

**[Muhammad Zeeshan Islam](https://github.com/zeeshan020dev)**

Co-Founder – [Unicodrex](https://www.linkedin.com/company/unicodrex/) | Technical Lead – [Skill Sprint](https://www.linkedin.com/company/skill-sprint-pk/) | Trainee – CEGA

[![GitHub](https://img.shields.io/badge/GitHub-zeeshan020dev-black?logo=github)](https://github.com/zeeshan020dev)

**[Rana Ali Husnain](https://github.com/AliHusnain05)**

[![GitHub](https://img.shields.io/badge/GitHub-AliHusnain05-black?logo=github)](https://github.com/AliHusnain05)

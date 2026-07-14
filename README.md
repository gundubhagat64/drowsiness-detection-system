# 🚗 Driver Drowsiness Detection System

An AI-powered Driver Drowsiness Detection System developed using Python, OpenCV, dlib, and Computer Vision. This project monitors the driver's eye movements in real time and alerts the driver with an alarm when drowsiness is detected, helping reduce road accidents caused by fatigue.

---

## 📌 Features

- 👁️ Real-time eye detection using webcam
- 😴 Eye Aspect Ratio (EAR) based drowsiness detection
- 🔔 Instant alarm when eyes remain closed for a specific duration
- 🎯 Facial landmark detection using dlib
- ⚡ Fast and accurate real-time monitoring
- 💻 Easy to run and customize

---

## 🛠️ Technologies Used

- Python
- OpenCV
- dlib
- NumPy
- SciPy
- imutils
- pygame

---

## 📂 Project Structure

```
Drowsiness_Detection/
│
├── models/
│   └── shape_predictor_68_face_landmarks.dat
│
├── Drowsiness_Detection.py
├── alarm.wav
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/gundubhagat64/drowsiness-detection-system.git
```

### Move into Project

```bash
cd drowsiness-detection-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python Drowsiness_Detection.py
```

---

## 📥 Download Required Model

Download the **shape_predictor_68_face_landmarks.dat** file from the official dlib model repository and place it inside the **models/** folder before running the project.

---

## 📸 Working

1. Webcam captures the driver's face.
2. Facial landmarks are detected.
3. Eye Aspect Ratio (EAR) is calculated.
4. If the eyes remain closed for a predefined number of frames, the system detects drowsiness.
5. An alarm sound alerts the driver immediately.

---

## 🚀 Future Enhancements

- 📍 Live GPS Tracking
- 📱 SMS Alert to Emergency Contact
- ☁️ Cloud Database Integration
- 📊 Driver Monitoring Dashboard
- 🌙 Night Vision Support
- 📈 AI-based Drowsiness Prediction
- 📹 Video Recording during Drowsiness Detection

---

## 💡 Applications

- Smart Vehicles
- Driver Safety Systems
- Transport Industry
- Fleet Management
- Accident Prevention

---

## 👨‍💻 Author

**Gundu Ekanath Bhagat**

- GitHub: https://github.com/gundubhagat64
- LinkedIn: https://www.linkedin.com/in/gundubhagat2004/

---

## ⭐ If you like this project, don't forget to Star this repository!

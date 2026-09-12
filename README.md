# AI Virtual Mouse Using Hand Gestures

An AI-powered virtual mouse that allows users to control their computer using hand gestures captured through a webcam. The project uses computer vision and hand tracking to detect finger movements and translate them into mouse actions.

## Features

- Real-time hand tracking using MediaPipe
- Index finger-based cursor movement
- Thumb and index finger pinch gesture for left click
- Index + middle finger gesture for scrolling up
- Index + middle + ring finger gesture for scrolling down
- Smooth cursor movement using coordinate interpolation
- Webcam-based, touch-free computer interaction

## Technologies Used

- **Python**
- **OpenCV** – Webcam access and image processing
- **MediaPipe** – Hand landmark detection and finger tracking
- **PyAutoGUI** – Computer mouse control
- **Math** – Distance calculation between hand landmarks

## Project Structure

```text
AI-Virtual-Mouse/
│
├── main.py
├── hand_tracking.py
├── README.md
├── requirements.txt
└── .gitignore
```

### File Description

- `main.py` – Main application that opens the webcam and controls the mouse using detected gestures.
- `hand_tracking.py` – Handles MediaPipe hand detection, landmark positions, finger recognition, and fingertip distance calculation.
- `README.md` – Project documentation.
- `requirements.txt` – Required Python libraries.
- `.gitignore` – Files and folders that should not be uploaded to GitHub.

## Gesture Controls

| Hand Gesture | Action |
|---|---|
| ☝️ Index finger only | Move cursor |
| 🤏 Thumb + Index finger close | Left click |
| ✌️ Index + Middle fingers | Scroll up |
| 🖖 Index + Middle + Ring fingers | Scroll down |

## How It Works

The webcam captures the user's hand in real time. MediaPipe detects 21 hand landmarks and provides their coordinates. The program uses these coordinates to recognize finger positions and gestures.

For cursor movement, the index fingertip is tracked and its camera coordinates are converted into screen coordinates. PyAutoGUI then moves the system cursor to the corresponding position.

For clicking, the distance between the thumb tip and index fingertip is calculated. When the fingers come close enough, a left mouse click is triggered.

Different combinations of raised fingers are used to control scrolling.

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Hand Landmarks
   ↓
Finger/Gesture Recognition
   ↓
PyAutoGUI
   ↓
Mouse Control
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse
```

Replace `your-username` with your GitHub username.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install opencv-python mediapipe pyautogui
```

### 4. Run the Project

```bash
python main.py
```

Make sure your webcam is connected and accessible.

## Requirements

- Python 3.11 is recommended for this project.
- A working webcam
- Windows/Linux/macOS computer
- Internet connection for installing Python packages

## Important Notes

- Keep your hand clearly visible to the webcam.
- Good lighting improves hand tracking accuracy.
- Cursor movement may vary depending on camera position and lighting.
- PyAutoGUI controls the actual system mouse, so use the click gestures carefully.
- Press **Q** to exit the webcam application.

## Future Improvements

- Right-click gesture
- Double-click gesture
- Drag and drop
- Better scroll control based on hand movement direction
- Improved cursor stabilization
- Multi-hand gesture support
- Volume and brightness control
- Customizable gestures
- Application-specific shortcuts

## Learning Outcomes

This project helped develop practical knowledge of:

- Computer Vision
- OpenCV
- MediaPipe Hand Tracking
- Hand Landmark Detection
- Gesture Recognition
- Coordinate Mapping
- Mouse Automation
- Real-Time Video Processing
- Human-Computer Interaction

## License

This project is created for educational and learning purposes.

---

**Developed as a Computer Vision project using Python.**

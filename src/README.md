# Autonomous Vehicle Control with Raspberry Pi and OpenCV

This repository contains the essential Python modules used in our WRO 2025 Future Engineers project. The project integrates **real-time computer vision** with **GPIO-based motor control** to create an autonomous vehicle capable of recognizing traffic markers and navigating accordingly.

## 🧠 Project Structure

### 1. `OpenCv+Cam_2.py`
This script handles real-time **color detection** using the Raspberry Pi Camera and OpenCV. It converts each frame from BGR to HSV color space and applies color masking to detect **red** and **green** objects. Based on the amount of detected color area:

- If red is dominant, the system interprets a **"Stop or Turn"** signal.
- If green is dominant, the system continues **moving forward**.
- If no significant color is detected, the system displays `"RENK YOK"` on the screen.

> This module provides visual input to guide movement decisions based on WRO track signals.

### 2. `MotorControl.py`
This module defines a simple interface for motor commands via Raspberry Pi GPIO pins. It allows:

- `ileri()` – Move forward  
- `geri()` – Move backward  
- `sag()` – Turn right  
- `sol()` – Turn left  
- `dur()` – Stop the motors

PWM control is implemented on the ENA and ENB pins to regulate motor speed.

> The motor control logic is separated from the vision module for modularity and ease of debugging.

## ⚙️ Hardware Compatibility

- Raspberry Pi 4 Model B
- L298N Motor Driver
- 2x DC Motors
- LiPo Battery with 5V Buck Converter
- Pi Camera Module

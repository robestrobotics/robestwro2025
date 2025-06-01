# 🚗 Color and Distance-Based Robot Control

This project is a Python-based robot control system using a Raspberry Pi, OpenCV, and basic GPIO interfacing to create a color-detecting and obstacle-avoiding autonomous vehicle.

## 📌 Project Summary

The robot moves forward and reacts to color signals and obstacles in its environment:

* **Red**: Turns right
* **Green**: Turns left
* **Obstacle within 50 cm**: Turns left to avoid
* Otherwise: Moves forward for three successful turns

## 🧠 Technologies Used

* **Python 3**
* **OpenCV** for image processing
* **RPi.GPIO** for motor and sensor control
* **Raspberry Pi Camera Module** or USB webcam

## 🔧 Hardware Setup

* **DC Motor** controlled via `IN1`, `IN2`, and `ENA` pins
* **Ultrasonic Sensor** using `TRIG` (GPIO 5) and `ECHO` (GPIO 6)
* **Raspberry Pi GPIO Pins**

## 🎯 Logic Overview

1. **Video Capture**: Captures frames from the camera.
2. **Color Detection**: Detects red and green objects in the frame using HSV color thresholds.
3. **Ultrasonic Sensor**: Measures distance to obstacles.
4. **Motion Control**: Uses direction logic based on color or distance.

## 📄 How It Works

```python
if red_area > 1000:
    turn right, then go forward
elif green_area > 1000:
    turn left, then go forward
elif distance <= 50:
    avoid by turning left
else:
    go forward and increase counter
```

* Each successful forward movement increments a counter
* Loop ends after 3 valid movements

## 🚦 Motor Control Functions

* `motor_ileri(hiz=70)`: Moves the robot forward
* `motor_dur()`: Stops all motor movement
* `motor_sola_don(hiz=60)`: Turns the robot left
* `motor_saga_don(hiz=60)`: Turns the robot right

## 📏 Distance Measurement

The `mesafe_olc()` function uses ultrasonic TRIG and ECHO timing to calculate the distance in centimeters.

## 🛑 Cleanup

The system ensures clean GPIO state at the end:

```python
GPIO.cleanup()
```

## ⚠️ Safety Note

Use on a safe surface; robot is not aware of height differences like stairs or edges.

## 📦 Future Improvements

* Add logging or telemetry
* Implement more color types (blue, yellow, etc.)
* Use PID for smoother motor control
* Add real-time plotting or camera overlay

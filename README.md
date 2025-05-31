# 🤖 Smart Autonomous Robot

A Raspberry Pi–powered prototype that combines sensor feedback, motor control, and real-time image processing for autonomous decision-making.

## 📚 Table of Contents

* [Overview](#-overview)
* [Hardware Components](#-hardware-components)
* [Control and Processing](#-control-and-processing-raspberry-pi)
* [Power Management](#-power-management)
* [Software](#-software)
* [Challenges and Solutions](#-challenges-and-solutions)
* [Conclusion](#-conclusion)

## 📌 Overview

Our robot is equipped with a **DC motor** for basic movement and an **MG90S micro servo motor** for steering control. These motors enable the robot to interact with its environment through different tasks. The entire system is managed by a **Raspberry Pi** microcomputer. To enhance environmental awareness, the robot utilizes an **HC-SR04 ultrasonic sensor** and a **ONEZERO Model 806 camera** for real-time image processing. With this combination, the robot can detect **red and green obstacles**, make decisions, and command its motors accordingly.

## 🧰 Hardware Components

### ⚙️ DC Motor and L298N Motor Driver

The robot's movement system is powered by a **DC motor**, which is controlled via the **L298N motor driver**. This driver enables forward and backward motion with ease. Known for its high current capacity and dual H-bridge design, L298N is commonly used in robotics. A **12V LiPo battery** powers this module, ensuring stable energy delivery while reducing load on the Raspberry Pi.

### 🔄 MG90S Micro Servo Motor

The **MG90S servo motor** manages the robot's steering. Compact and capable of rotating up to 180°, it is ideal for precise control. The **Raspberry Pi** controls the servo via **PWM signals**, where pulse width sets the motor's angle. Precise PWM generation is crucial for smooth operation.

### 📏 HC-SR04 Ultrasonic Sensor

To perceive its surroundings, the robot employs an **HC-SR04 ultrasonic sensor**. It calculates distance using echo time. A high TRIG signal sends out an ultrasonic pulse, which reflects off obstacles and returns to the ECHO pin. The round-trip time is used to compute distance—ideal for **obstacle avoidance** and **wall-following**.

### 📸 ONEZERO Model 806 Camera Module

For image processing, the **ONEZERO Model 806 camera** is used. Compatible with Raspberry Pi, this high-resolution camera enables **object detection**, **color tracking**, and **decision-making**. Visual data is processed using **Python** and **OpenCV**, empowering the robot to respond to visual cues.

## 🧠 Control and Processing: Raspberry Pi

All components are coordinated by the **Raspberry Pi**, offering powerful processing in a compact board. Its **GPIO pins** allow for flexible input/output setups, supporting **PWM**, **digital**, and other protocols. This enables unified motor and sensor control.

## 🔋 Power Management

Efficient energy distribution is vital. A **12V LiPo battery** powers the DC motor and L298N, protecting the Raspberry Pi. The **5V regulator** on L298N supports low-power components. The **servo motor** draws power from a separate supply, improving stability.

## 💻 Software

Development is done in **Python**. Scripts manage sensor data reading, servo control, and camera image processing. The robot can **react to nearby objects** and **track colors**. With machine learning, the system can evolve for **complex decision-making**.

## 🚧 Challenges and Solutions

During development, we tackled issues like **component communication**, **power interference**, and **sensor accuracy**:

* Shared power caused servo jitter → resolved with a **separate voltage regulator**
* Ultrasonic sensor placement and echoes affected accuracy → fixed with **optimized positioning**

## ✅ Conclusion

This robot system is a **functional prototype**, integrating hardware and responsive software. It can be extended with **LiDAR**, **advanced cameras**, and **wireless modules**, paving the way for **smart autonomous systems**.

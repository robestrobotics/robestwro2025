## System Overview

This autonomous vehicle is designed using a **Raspberry Pi 4 Model B** as its main controller (SBC). It features a **DC motor** driven via an **L298N motor driver** module and uses a **camera module** for visual input. The robot uses **OpenCV** to detect **red and green colors** and navigates accordingly by adjusting the motor directions.

The power system is based on a **LiPo battery**, which provides energy for the whole system. A **step-down voltage regulator** is used to supply a stable 5V to the Raspberry Pi, ensuring reliable operation without voltage drops.

---

### 🔧 Key Components

- **Controller:** Raspberry Pi 4 Model B (SBC)
- **Motor Driver:** L298N Dual H-Bridge
- **Motors:** 2x DC Motors (Drive motors)
- **Camera:** Pi Camera Module
- **Software:** Python + OpenCV (for color detection)
- **Power Source:** LiPo Battery
- **Voltage Regulation:** Step-down Buck Converter (5V output)

---

### 🧠 Functionality

- The camera continuously detects **red** and **green** traffic markers (as used in WRO Future Engineers challenge).
- Upon detection:
  - **Green** → Continue in the same direction.
  - **Red** → Turn around and complete the third lap in reverse direction.
- The robot runs **fully autonomously** after activation.
- No wireless communication or manual control is used during the run (in accordance with WRO rules).

---

> ✅ This setup complies with the WRO 2025 "Future Engineers" category rules regarding autonomous behavior, component selection, and documentation requirements.

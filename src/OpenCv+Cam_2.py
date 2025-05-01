import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)

    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    red_area = cv2.countNonZero(red_mask)
    green_area = cv2.countNonZero(green_mask)

    if red_area > 1000:
        color_text = "KIRMIZI"
        color = (0, 0, 255)
    elif green_area > 1000:
        color_text = "YESIL"
        color = (0, 255, 0)
    else:
        color_text = "RENK YOK"
        color = (200, 200, 200)

    cv2.putText(frame, color_text, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 4)

    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
 # In this file we make a class that will inform us about the state of the control hand
 # This information should then determine at what point should the stimulation be delivered

import mediapipe as mp
import numpy as np
import cv2
import matplotlib.pyplot as plt

hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cv_object  = cv2.VideoCapture(0)

while cv_object.isOpened():
    ret, frame = cv_object.read()

    if not ret:
        continue

    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow('?', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv_object.release()
cv2.destroyAllWindows()

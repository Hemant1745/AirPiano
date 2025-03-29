import cv2
import mediapipe as mp
import threading
import cvzone.HandTrackingModule 
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_Styles
mphands=mp.solutions.hands

cap=cv2.VideoCapture(0)
hands=mphands.Hands()
while True:
    data,image=cap.read()
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    results=hands.process(image)
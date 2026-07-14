import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from imutils import face_utils
import imutils
import pygame
from datetime import datetime

# ---------------- Alarm Setup ----------------
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")

def sound_alarm():
    pygame.mixer.music.play(-1)

def stop_alarm():
    pygame.mixer.music.stop()


# ---------------- Eye Aspect Ratio Function -----
def eye_aspect_ratio(eye):

    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear


# ---------------- Settings -------
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 30

COUNTER = 0
ALARM_ON = False


print("Loading facial landmark detector...")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


print("Starting camera...")

cap = cv2.VideoCapture(0)

# ---------------- Main Loop ------------
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = imutils.resize(frame, width=900)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull], -1, (0,255,0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0,255,0), 1)

        # ---------------- Drowsiness Logic ----------------
        if ear < EYE_AR_THRESH:

            COUNTER += 1

            if COUNTER >= EYE_AR_CONSEC_FRAMES:

                if not ALARM_ON:
                    ALARM_ON = True
                    sound_alarm()

                cv2.putText(frame, "DROWSINESS ALERT!",
                            (10,30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0,0,255),
                            2)

                # Red Border Warning
                cv2.rectangle(frame,(0,0),(900,500),(0,0,255),6)

        else:

            COUNTER = 0

            if ALARM_ON:
                stop_alarm()

            ALARM_ON = False


        cv2.putText(frame, "EAR: {:.2f}".format(ear),
                    (300,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,255,0),
                    1)


    # ---------------- Current Time ----------------
    current_time = datetime.now().strftime("%H:%M:%S")

    cv2.putText(frame, current_time,
                (750,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)


    cv2.imshow("Driver Drowsiness Detector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
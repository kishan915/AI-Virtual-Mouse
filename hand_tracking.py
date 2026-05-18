#Day 2 Task
import cv2
import mediapipe as mp
import math


class handDetector():

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands()

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    img,
                    handLms,
                    self.mpHands.HAND_CONNECTIONS
                )

        return img
#Day 3 task
    def findPosition(self, img):

        self.lmList = []

        if self.results.multi_hand_landmarks:

            myHand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(myHand.landmark):

                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)

                self.lmList.append([id, cx, cy])

        return self.lmList  
    #day 4 task 
    def fingersUp(self):

        fingers = []

        # Thumb
        if self.lmList[4][1] > self.lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        tipIds = [8, 12, 16, 20]

        for id in tipIds:

            if self.lmList[id][2] < self.lmList[id - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
    #Day 4 task end
    #Day 6 task
    def findDistance(self, p1, p2, img):

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)

            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            return length, img
    #Day 6 task end

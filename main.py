import cv2
import hand_tracking as htm
import pyautogui
import time
#Day 7 task
prevX = 0
prevY = 0

smoothening = 7
frameR = 100
#Day 7 task end

pyautogui.FAILSAFE = False
screenWidth, screenHeight = pyautogui.size()

cap = cv2.VideoCapture(0)

detector = htm.handDetector()

while True:

    success, img = cap.read()

    img = detector.findHands(img)
#Day 3 task
    lmList = detector.findPosition(img)
    #Day 4 task
    if len(lmList) != 0:
        #Dayq 6 task
        length, img = detector.findDistance(4, 8, img)

        if length < 40:

            pyautogui.click()
            time.sleep(0.3)

            cv2.circle(img, (50, 50), 15, (0, 255, 0), cv2.FILLED)
        #Day 6 task endq
        fingers = detector.fingersUp()
        if fingers[1] == 1 and fingers[2] == 1:
            pyautogui.scroll(-50)

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            pyautogui.scroll(50)

        #Day 5 task
        if fingers[1] == 1 and fingers[2] == 0:
            print("Move Mode")

            x1 = lmList[8][1]
            y1 = lmList[8][2]

            #screenX = screenWidth / 640 * x1
            #screenY = screenHeight / 480 * y1 replace with below 2 lines for better control of mouse movement
            screenX = (x1 - frameR) * screenWidth / (640 - 2 * frameR)

            screenY = (y1 - frameR) * screenHeight / (480 - 2 * frameR)

            #pyautogui.moveTo(screenX, screenY)  replace this with below 4 lines for smoothening the mouse movement
        #day 5 task end
        #day 7 task
            currX = prevX + (screenX - prevX) / smoothening
            currY = prevY + (screenY - prevY) / smoothening

            pyautogui.moveTo(currX, currY)

            prevX, prevY = currX, currY
        #day 7 task end
        

        #print(fingers) repleace it with, if fingers[1] == 1 and fingers[2] == 0:
        
    #Day 4 task end
    """
I can remove this part this is for only when i went to test the position of the landmarks and to see if the code is working or not.
    if len(lmList) != 0:

        print(lmList[8])

        x = lmList[8][1]
        y = lmList[8][2]
        cv2.circle(img, (x, y), 15, (255, 0, 255), cv2.FILLED)
#End of Day 3 task
"""
#day 7 task
    cv2.rectangle(img, (frameR, frameR),
              (640 - frameR, 480 - frameR),
              (255, 0, 255), 2)
#day 7 task end
    cv2.imshow("AI Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
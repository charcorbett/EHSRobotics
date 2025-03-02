
import cv2
from cvzone.HandTrackingModule import HandDetector 
from cvzone.SerialModule import SerialObject
mySerial = SerialObject("COM7", 9600, 1)
detector=HandDetector(detectionCon=0.8,maxHands=1)
cap = cv2.VideoCapture(0)


while True:
    success, img1 = cap.read()
    hands,img = detector.findHands(img1)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        #print(fingerUp)
        mySerial.sendData(fingerUp) 
    cv2.imshow("image", img)
    cv2.waitKey(1)

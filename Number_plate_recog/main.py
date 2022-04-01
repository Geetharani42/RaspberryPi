import cv2
import numpy as np
import pytesseract
from PIL import Image
import time

cam = cv2.VideoCapture(0)
time.sleep(2)
while True:
            ret,frame = cam.read()
            cv2.imshow('webcam', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials 
            gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise

            original = pytesseract.image_to_string(gray, config='-l eng --oem 3 --psm 12')
            print (original)

            if cv2.waitKey(1)&0xFF == ord('q'):
                break
cam.release()
cv2.destroyAllWindows() 
        

 

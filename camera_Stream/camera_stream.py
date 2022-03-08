#Libraries importing
import cv2          #cv2 library for camera
from time import sleep

#accessing camera
cam  =  cv2.VideoCapture(0)

#main loop
while True:
          #camera reading
            ret,frame = cam.read()
          #displaying video streaming in new window
           cv2.imshow("video stream",frame)
          #keyboard interrupt to break the loop by giving q input from keypad
           if cv2.waitKey(1)&0xFF==ord('q'):
                      break
#camera reading stopped
cam.release()
#camera window closed
cv2.destroyAllWindows()
#Libraries
import numpy as np
import imutils
import cv2
import time


prototxt ="MobileNetSSD_deploy.prototxt.txt"
model ="MobileNetSSD_deploy.caffemodel"
confThresh = 0.2

CLASSES=["background","aeroplane","bicycle","bird","boat",
       "bottle","bus","car","cat","chair","cow","diningtable",
       "dog","horse","motorbike","person","spectacles","pen","handkerchief",
         "earphones","note book","Mouse","keyboard","TvMonitor","box","sofa","train","steps"]
COLORS=np.random.uniform(0, 225, size=(len(CLASSES), 3))
print("loading model...")
net=cv2.dnn.readNetFromCaffe(prototxt , model)
print("starting camera feed....")
vs=cv2.VideoCapture(0)
time.sleep(0.2)


while True:
    __,frame=vs.read()
    frame = imutils.resize(frame, width=500)
    (h, w) = frame.shape[:2]
    imResize=cv2.resize(frame, (300, 300))
    blob=cv2.dnn.blobFromImage(imResize,0.007843,(300,300),127.5)
    net.setInput(blob)
    detections=net.forward()
    detShape=detections.shape[2]
    for i in np.arange(0,detShape):
        confidence=detections[0,0,i,2]

        if confidence > confThresh:
            idx=int(detections[0,0,i,1])
            #print("ClassId",detections[0,0,i,1])
            #print(COLORS[idx])
            box=detections[0,0,i,3:7] * np.array([w,h,w,h])
            (startX, startY, endX, endY)= box.astype("int")
            label="{}:{:.2f}%".format(CLASSES[idx],confidence*100)
            cv2.rectangle(frame,(startX,startY),(endX,endY),COLORS[idx],2)
            y=0
            if startY-15>15:
                y=startY-15
            else:
                startY+15
            obj="{}".format(CLASSES[idx])
            print(obj)
            cv2.putText(frame,label,(startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,COLORS[idx],2)
    cv2.imshow("frame",frame)
            
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
vs.release()
cv2.destroyAllWindows()

        
    

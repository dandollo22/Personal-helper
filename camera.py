import cv2
import numpy as np
import os
import time
# Open the device at the ID 0

cap = cv2.VideoCapture(1)

#Check whether user selected camera is opened successfully.
#10
if not (cap.isOpened()):

    print("Could not open video device")
while(True):

# Capture frame-by-frame

      ret, frame = cap.read()
      hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      low=np.array([161,155,84])
      high=np.array([179,255,255])
      redx=cv2.inRange(hsv_frame,low,high)
      contours,x =cv2.findContours(redx, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      mid=0
      for cnt in sorted(contours,key=lambda x:cv2.contourArea(x),reverse=1):
          (a,b,c,d)=cv2.boundingRect(cnt)
          mid=int((a+a+c)/2)
          break;
     
      cv2.line(frame,(mid,0),(mid,480),(0,255,0),2)
# Display the resulting frame

      cv2.imshow('preview',frame)
      cv2.imshow("mask",redx)
#Waits for a user input to quit the application

      if cv2.waitKey(1) & 0xFF == ord('q'):

             break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()

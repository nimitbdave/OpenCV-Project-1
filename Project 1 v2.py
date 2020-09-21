#Project 1

#Task 1: Show the webcam video feed on screen.
import cv2
frameWidth = 640
frameHeight = 480                 #setting the width and height of the frame
cap = cv2.VideoCapture(1)         #set device to 1
cap.set(3, frameWidth)            #at ID #3
cap.set(4, frameHeight)           #at ID #4
cap.set(10,150)                   #set brightness at 150

#Task 2:  Color detection.
#Find different types of colors.
def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    #Convert image to HSV
    lower = np.array([h_min,s_min,v_min])           #lower limit
    upper = np.array([h_max,s_max,v_max])           #upper limit
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("img",mask)                          #check to see if working properly
    
while True:
    success, img = cap.read()                 #get image
    cv2.imshow("Result",img)                  #display it using imshow
    if cv2.waitKey(1) & 0xFF == ord('q'):     
      break                                   #webcam feed now visible

       

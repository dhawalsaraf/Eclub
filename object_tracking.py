import cv2 
import numpy as np 

cam = cv2.VideoCapture(0)

hh = 56
hl = 34
sh = 175
sl = 73
vh = 255
vl = 167

def huehigh(val):
    global hh
    hh = val

def huelow(val):
    global hl
    hl = val

def sathigh(val):
    global sh
    sh = val

def satlow(val):
    global sl
    sl = val

def valhigh(val):
    global vh
    vh = val

def vallow(val):
    global vl
    vl = val

cv2.namedWindow("Trackbar")

cv2.createTrackbar("HueHigh","Trackbar",0,360,huehigh)
cv2.createTrackbar("HueLow","Trackbar",0,360,huelow)
cv2.createTrackbar("SatHigh","Trackbar",0,255,sathigh)
cv2.createTrackbar("SatLow","Trackbar",0,255,satlow)
cv2.createTrackbar("ValHigh","Trackbar",0,255,valhigh)
cv2.createTrackbar("ValLow","Trackbar",0,255,vallow)


while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(500,350))
    frame_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    Upperbound = np.array([hh,sh,vh])
    Lowerbound = np.array([hl,sl,vl])
    print(Upperbound,Lowerbound)
    mask = cv2.inRange(frame_HSV,Lowerbound,Upperbound)

    myselection = cv2.bitwise_and(frame,frame,mask = mask) #syntax hi aisa h 

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("My selection",myselection)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

cam = cv2.VideoCapture(0)

ignore,initial_frame = cam.read()

while True:
    ignore,frame = cam.read()

    Upperbound = np.array([hh,sh,vh])
    Lowerbound = np.array([hl,sl,vl])

    mask = cv2.inRange(frame,Lowerbound,Upperbound)
    dup=mask.copy()
    contours, hierarchy = cv2.findContours(image=dup, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    

    cv2.drawContours(image=frame, contours=contours, contourIdx=-1, color=(0,0, 255), thickness=2, lineType=cv2.LINE_AA)
    #myselection = cv2.bitwise_and(frame,frame,mask = mask) #syntax hi aisa h 
    print(Upperbound,Lowerbound)
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()  
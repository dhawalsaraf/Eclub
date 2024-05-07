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

# Capture the initial frame


while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (500, 350))
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    Upperbound = np.array([hh, sh, vh])
    Lowerbound = np.array([hl, sl, vl])
    print(Upperbound, Lowerbound)
    mask = cv2.inRange(frame_HSV, Lowerbound, Upperbound)

    myselection = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("My selection", myselection)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cam = cv2.VideoCapture(0)
ignore, initial_frame = cam.read()
while True:
    ignore, frame = cam.read()

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    Upperbound = np.array([hh, sh, vh])
    Lowerbound = np.array([hl, sl, vl])

    mask = cv2.inRange(frame_HSV, Lowerbound, Upperbound)
    inversemsk = cv2.bitwise_not(mask)

    cloak = cv2.bitwise_and(initial_frame, initial_frame, mask=inversemsk)
    background = cv2.bitwise_and(frame, frame, mask=mask)
    final = cv2.bitwise_or(cloak, background)

    cv2.imshow("Cloak", cloak)
    cv2.imshow("Background", background)
    cv2.imshow("Final", final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

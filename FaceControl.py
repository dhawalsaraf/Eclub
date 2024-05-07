
import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pag

print(cv2.__version__)
width=640
height=480
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 120)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceMesh = mp.solutions.face_mesh.FaceMesh(False,3,False,.5,.5)
# 1 --static image
# max no. of faces 
mpDraw = mp.solutions.drawing_utils
drawSpecCircle = mpDraw.DrawingSpec(thickness=3,circle_radius=2,color=(255,0,0))
drawSpecLine = mpDraw.DrawingSpec(thickness=1,circle_radius =2,color=(0,0,255))

class mpfacemesh :
    import mediapipe as mp
    def __init__(self,Static=False,max_faces=3,tol1=.5,tol2=.5):
        self.facemesh=self.mp.solutions.face_mesh.FaceMesh(Static,max_faces,False,tol1,tol2)
    def Facemeshlandmarks(self,frame):
        frameRGB= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        landmarks=[]
        results = self.facemesh.process(frameRGB)

        if results.multi_face_landmarks !=None:
            for landmark in results.multi_face_landmarks:
                mpDraw.draw_landmarks(blank,landmark,mp.solutions.face_mesh.FACEMESH_CONTOURS,drawSpecCircle,drawSpecLine)
                counter=0
                location=[]
                for lm in landmark.landmark:
                    #cv2.putText(frame,str(counter),(int(lm.x*width),int(lm.y*height)),font,fontsize,fontColor,fonthickness)
                    counter+=1
                    location.append((int(lm.x*width),int(lm.y*height)))
                landmarks.append(location)
        return landmarks



font = cv2.FONT_HERSHEY_SIMPLEX
fontsize=.2
fontColor = (0,255,255)
fonthickness = 1
facemeshobj = mpfacemesh()  
px, py = 0, 0
diff = 0
screenx, screeny = pag.size()
while True:
    ignore,  frame = cam.read()
    blank = np.zeros(frame.shape,dtype='uint8')
    landmarks = facemeshobj.Facemeshlandmarks(frame)
    for face in landmarks:
        # print("forehead", face[8])
        # print("upperlip", face[0])
        # print("lowerlip", face[18])
        actual_x, actual_y = face[8][0]*screenx/width, face[8][1]*screeny/height
        if px == 0 and py == 0:
            px, py = face[8]
        else:
            pag.moveTo(actual_x, actual_y)
        if diff == 0:
            diff = abs(face[0][1] - face[18][1])
        elif abs(face[0][1] - face[18][1]) > (diff * 1.33):
            pag.click()
        for location in face: 
            cv2.circle(frame,(location[0],location[1]),3,fontColor,-1)
        cv2.circle(frame, (face[8][0], face[8][1]), 3, (0, 0, 255), -1)
        cv2.circle(frame, (face[18][0], face[18][1]), 3, (255, 0, 0), -1)
        cv2.circle(frame, (face[0][0], face[0][1]), 3, (255, 0, 0), -1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
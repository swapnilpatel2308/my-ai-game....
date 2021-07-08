import cv2
import mediapipe as mp
import numpy as np
import random
from playsound import playsound
import time
number1=0
number2=0
mypoint=0
computerpoint=0
i=0
j=0
code=1
speed=5
mycode=1
cap = cv2.VideoCapture(0)
position=random.randrange(50,1100,20)
position1=random.randrange(50,1100,15)
position2=random.randrange(50,1100,25)
position3 = random.randrange(50,1100,30)
position4 = random.randrange(50,1100,50)
position5 = random.randrange(50,1100,35)
position6 = random.randrange(50,1100,54)
position7 = random.randrange(50,1100,42)
bgi=np.zeros((500,700,3),np.uint8)
mphands= mp.solutions.hands
hands=mphands.Hands()
mpDraw=mp.solutions.drawing_utils


while True:
    success,img = cap.read()
    img=cv2.flip(img,1)
    img=cv2.resize(img,(1300,650))
    
    backgroundimg = np.zeros_like(img)
    #hand point control
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgrgb)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)

                if id==12:
                    #cv2.circle(img,(cx,cy),25,(0,0,255),cv2.FILLED)
                    number1=cx
                    number2=cy
    cv2.circle(img,(20,100),10,(255,0,0),-1)
    cv2.putText(img,"+1 point",(40,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(200,100),10,(0,0,255),-1)
    cv2.putText(img,"-3 point",(210,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(360,100),10,(255,255,0),-1)
    cv2.putText(img,"+1 speed",(370,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(540,100),10,(0,255,255),-1)
    cv2.putText(img,"-5 point",(550,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(700,100),10,(0,102,102),-1)
    cv2.putText(img,"+2 point",(710,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(860,100),10,(102,204,0),-1)
    cv2.putText(img,"-5 speed",(870,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.circle(img,(1060,100),10,(0,0,0),-1)
    cv2.putText(img,"0 score",(1070,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)

    cv2.circle(img,(30,50),10,(0,255,0),-1)
    cv2.putText(img,f'my point : {int(mypoint)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3,cv2.LINE_AA)

    cv2.circle(img,(300,50),10,(0,255,0),-1)
    cv2.putText(img,f'computer point : {int(computerpoint)}',(320,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3,cv2.LINE_AA)

    
    if(mycode==1):
        cv2.circle(img,(position,i+5),20,(255,0,0),-1)        #blue +1 point
        i=i+speed
        cv2.rectangle(img,(number1,500),(number1+200,550),(0,255,0),-1)
        if(i>500 and i<=550 and number1<=position and number1>=position-200):
            mypoint=mypoint+1
            i=0
            position=random.randrange(50,1100,20)
            speed=speed+3
            playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)
        
            
        if(i>=550):
            i=0
            computerpoint=computerpoint+1
            position=random.randrange(50,1100,20)
            

        if mypoint>=3 and mypoint<=5:
            cv2.circle(img,(position1,i+5),20,(255,255,0),-1)                   #speed up +1 perpal blur
            if(i>500 and i<=550 and number1<=position1 and number1>=position1-200):
                mypoint=mypoint+1
                i=0
                position1=random.randrange(50,1100,20)
                speed=speed+4
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint>=5 and mypoint<=7:                                   #-3 point  red
            cv2.circle(img,(position2,i+5),20,(0,0,255),-1)
            if(i>500 and i<=550 and number1<=position2 and number1>=position2-200):
                mypoint=mypoint-3
                i=0
                position2=random.randrange(50,1100,20)
                speed=speed+2
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint>=8 and mypoint<10:                           #-5 point and speed up  yellow
            cv2.circle(img,(position3,i+5),20,(0,255,255),-1)
            if(i>500 and i<=550 and number1<=position3 and number1>=position3-200):
                mypoint=mypoint-5
                i=0
                position3=random.randrange(50,1100,20)
                speed=speed+5
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint>=8 and mypoint<=10:                           #+2 point  yellow
            cv2.circle(img,(position4,i+5),20,(0,102,102),-1)
            if(i>500 and i<=550 and number1<=position4 and number1>=position4-200):
                mypoint=mypoint+2
                i=0
                position4=random.randrange(50,1100,20)
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint==12:                                         #speed slow  white
            cv2.circle(img,(position5,i+5),20,(102,204,0),-1)
            if(i>500 and i<=550 and number1<=position5 and number1>=position5-200):
                mypoint=mypoint+1
                position5=random.randrange(50,1100,20)
                speed=5
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint==12:
            cv2.circle(img,(position6,i+5),20,(0,0,0),-1)           #scour=0  black
            if(i>500 and i<=550 and number1<=position5 and number1>=position5-200):
                mypoint=0
                position6=random.randrange(50,1100,20)
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if mypoint>=15 and mypoint<=13:                       
            cv2.circle(img,(position7,i+5),20,(0,255,255),-1)
            if(i>500 and i<=550 and number1<=position7 and number1>=position7-200):
                mypoint=mypoint+1        
                position7=random.randrange(50,1100,20)
                speed=14
                playsound('C:\\Users\\SWAPNIL\\Desktop\\my project\\sound\\a.wav',block=False)

        if speed > 25:
            speed=10
        if(mypoint<=15 and computerpoint>=15):
            mycode=0
        if(mypoint>=15 and computerpoint<=15):
            mycode=2


    if(mycode==0):
        cv2.putText(img,"sorry you are fail in level 8 please try again",(350,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5,cv2.LINE_AA)
    if(mycode==2):
        cv2.putText(img,"congratulation you are win in level 8",(350,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5,cv2.LINE_AA)

    cv2.imshow("Image",img)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()
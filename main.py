import cv2
import time
import win32gui
import win32con
from os import mkdir

try:
    mkdir('footages')
except FileExistsError:
    pass


def minimizeWindow():    
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = video.get(3)
    height = video.get(4)
    print("Video resolution is", width, " X " , height)
    print("Help-- \n n1.Press Esc key to exit \n n2. Press m key to minimize")

    fourcc = cv2.VideoWriter_fourcc(*'H264')
    date_time = time.strftime("Recording : %H:%M %d-%m-%y")
    output = cv2.VideoWriter('footages/' + date_time + '.avc1',fourcc,20.0,(640,480))
    while video.isOpened():
        check,frame = video.read()
        if check == True:
            frame = cv2.flip(frame,1)
            t = time.ctime()
            cv2.rectangle(frame,(5,5,100,20),(255,255,255),cv2.FILLED)
            cv2.putText(frame,"Camera 1",(20,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),2)
            cv2.putText(frame,t,(420,460),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)

            cv2.imshow('CCTV camera',frame)
            output.write(frame)

            if cv2.waitKey(1) ==27:
                print("Video footage saved in current directory.\n Be safe & Secure")
                break
            elif cv2.waitKey(1) ==ord('m'):
                minimizeWindow()

        else:
            print("can't open this camera. select other or check its configuration.")
            break
    video.release()
    output.release()
    cv2.destroyAllWindows()

print("*"*80+"\n"+" "*30+"Welcome to CCTV software\n"+"*"*80)
ask = int(input('do you want to Start cctv ?\n1. Yes\n2. No\n>>> '))
if ask ==1:
    cctv()
elif ask ==2:
    print("ba bye! be safe & secure!")
    exit
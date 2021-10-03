import cv2
from random import randrange
#load pretrained data
trained_face_data= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to test
#img= cv2.imread('RDJ.png')
#img= cv2.imread('CAP.png')
#img= cv2.imread('rdj_cap.png')
#img= cv2.imread('BIG4.png')
#to capture video from webcam
webcam= cv2.VideoCapture(0)
##key= cv2.waitKey(1)
## Iterate forever over frames:
while True:
    #Read current frame
    successful_frame_read, frame = webcam.read()
    #convert to grayscales
    grayscaled_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangle around faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (randrange(128,256),randrange(128,256),randrange(128,256)), 2)

    cv2.imshow('Clever Prog Face Detector', frame)
    cv2.waitKey(1)
    key = cv2.waitKey(1)
    #Stop
    if key==81 or key==113:
        break
#release video capture
webcam.release()   
'''








#print(face_coordinates)


#Display image
cv2.imshow('Clever Programmer Face Detector',img)
cv2.waitKey()
'''

print("code completed")
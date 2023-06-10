# =============== using a config file

import cv2

face_cascade = cv2.CascadeClassifier('./config/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.5, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0),3)
    cv2.imshow('Face detection', img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

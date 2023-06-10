#==================== using cvzone

import cv2
from cvzone.FaceDetectionModule import FaceDetector
detector = FaceDetector()

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    _, bboxs = detector.findFaces(img)
    cv2.imshow('face detect', img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

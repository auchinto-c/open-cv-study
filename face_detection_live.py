import cv2 as cv

capture = cv.VideoCapture(1)
haar_path = 'haarcascade_frontalface_default.xml'

cascade = cv.CascadeClassifier(haar_path)

while True:
    ret, frame = capture.read()

    faces_rect = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
    
    cv.imshow('Detected', frame)

    if cv.waitKey(20) & 0xFF == 0:
        break

capture.release()
cv.destroyAllWindows()

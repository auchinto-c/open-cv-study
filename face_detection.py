import cv2 as cv

img = cv.imread('images/face.jpg')
# cv.imshow('Person', img)

haar_path = 'haarcascade_frontalface_default.xml'

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
 
haar_cascade = cv.CascadeClassifier(haar_path)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces detected: {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected', img)

cv.waitKey(0)
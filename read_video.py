import cv2 as cv

capture = cv.VideoCapture(1) # 0, 1, .. - Webcam; <path> can also be sent

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
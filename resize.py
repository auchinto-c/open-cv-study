# Rescaling - Changing the width/height of image / video frame

import cv2 as cv

img = cv.imread('images/AC.jpg')
cv.imshow('DP', img)

def rescaleFrame(frame, scale=0.75):
    # This works for images, videos and live video feeds

    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    dimensions = (w, h)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# def changeResolution(width, height):
#     # This only works for live video feed

#     capture.set(3, width)   # 3 -> Width setting
#     capture.set(4, height)  # 4 -> Height setting

cv.imshow('DP - Rescaled', rescaleFrame(img, 0.5))

cv.waitKey(0)

capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    cv.imshow('Video - Rescaled', rescaleFrame(frame, 0.5))

    if cv.waitKey(20) & 0xFF == 'd':
        break

capture.release()
cv.destroyAllWindows()
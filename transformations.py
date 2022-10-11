import cv2 as cv
import numpy as np

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0]) # shape[0] - height, shape[1] - width

    return cv.warpAffine(img, transMat, dimensions)

# x: +ve -> Right
# x: -ve -> Left
# y: +ve -> Down
# y: -ve -> Up

translated = translate(img, 50, 50)
cv.imshow('Translated', translated)

# Rotation

def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (w//2, h//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (w, h)

    return cv.warpAffine(img, rotMat, dimensions)

# angle : +ve -> Clockwise (CW)
# angle : -ve -> Counter-Clockwise (CCW)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resize)

# Cropping
crop = img[100:200, 100:300]
cv.imshow('Cropped', crop)

# Flipping
flip = cv.flip(img, 0) # 0 - Vertical, 1 - Horizontal, -1 - Vertical & Horizontal
cv.imshow('Flipped', flip)

cv.waitKey(0)
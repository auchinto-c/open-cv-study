import cv2 as cv

# Read Images
img = cv.imread('images/AC.jpg')

cv.imshow('DP', img)

cv.waitKey(0)
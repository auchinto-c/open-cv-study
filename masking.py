import cv2 as cv
import numpy as np

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (100, 100), (200, 400), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaoe Masked Image', masked)

cv.waitKey(0)
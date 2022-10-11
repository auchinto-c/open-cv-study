import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

# Basic operations on image
# ------------------------
green = blank.copy()
green[:] = 0, 255, 0
cv.imshow('Green', green)

partial = blank.copy()
partial[200:300, 300:400] = 0, 0, 255
cv.imshow('Partial', partial)

# Drawing a RECTANGLE
# ------------------------
rec1 = blank.copy()
cv.rectangle(rec1, (250, 250), (350, 450), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', rec1)

rec2 = blank.copy()
cv.rectangle(rec2, (250, 250), (350, 450), (0, 255, 0), thickness=cv.FILLED)  # Same Result if we set (thickness = -1)
cv.imshow('Rectangle - Filled', rec2)

# Drawing a CIRCLE
# ------------------------
cir = blank.copy()
cv.circle(cir, (200, 200), 50, (0, 0, 255), thickness = 3)
cv.imshow('Circle', cir)

# Drawing a LINE
# ------------------------
line = blank.copy()
cv.line(line, (100, 100), (400,400), (255, 0, 0), thickness=3)
cv.imshow('Line', line)

# Write a TEXT on an image
# ------------------------
txt = blank.copy()
cv.putText(txt, 'Hello', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', txt)

cv.waitKey(0)
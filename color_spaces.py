import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

# plt.imshow(img)
# plt.show()

# OpenCV reads image in BGR format
# Matplotlib treats images in RGB format
# OpenCV matrix shown by cv.imshow() appears in true colors
# OpenCV matrix shown by plt.imshow() appears in inverted colors

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('RGB', rgb) # Appears inverted
plt.imshow(rgb) # Appears in true color
plt.show()

# HSV to BGR
cv.imshow('HSV to BGR', cv.cvtColor(hsv, cv.COLOR_HSV2BGR))

# LAB to BGR
cv.imshow('LAB to BGR', cv.cvtColor(lab, cv.COLOR_LAB2BGR))

# There is no direct support available to change between color spaces like LAB and HSV.
# Convert sequentially via BGR: LAB -> BGR -> HSV

cv.waitKey(0)
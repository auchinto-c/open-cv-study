import cv2 as cv
from cv2 import INTER_AREA

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

# Converting to GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Adding BLUR
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT) # (2n+1, 2n+1) - Kernel size, this should always be Odd
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image (Smoothening/ Thickening the edges)
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding the image (Getting the edges back from a dilated image)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize the image
resize = cv.resize(img, (100, 100), interpolation=INTER_AREA) # INTER_LINEAR, INTER_CUBIC - Used when image scaled to larger dimensions. CUBIC is slowest but higher quality result
cv.imshow('Resized', resize)

# Crop the image
crop = img[50:200, 100:300]
cv.imshow('Cropped', crop)

cv.waitKey(0)
import cv2 as cv

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

# Averaging
avg = cv.blur(img, (3,3))
cv.imshow('Average Blur', avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
med = cv.medianBlur(img, 3)
cv.imshow('Median Blur', med)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
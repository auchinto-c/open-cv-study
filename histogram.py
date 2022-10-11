import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/AC.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

gray_masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Gray Masked', gray_masked)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

# Grayscale Histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# pixels')
hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Here gray_masked can't be passed into calcHist, since it will consider all the pixels which are black, which are lying outside the masked region.
# Since we just need to check the masked region, we need to explicitly specify the mask in calcHist.

plt.plot(hist)
plt.xlim([0, 256])

# Color Histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# pixels')
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
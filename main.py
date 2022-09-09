import cv2 as cv
import numpy as np


# read images
img = cv.imread("rice.bmp", cv.IMREAD_GRAYSCALE)  # gray image
imc = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)  # color image


cv.imshow("imageg",img)
cv.imshow("imagec",imc)


cv.waitKey(0)
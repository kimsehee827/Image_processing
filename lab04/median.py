import cv2 as cv
import numpy as np

img = cv.imread("pepper_noise.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H,W = img.shape[:]
median = np.zeros((H,W), img.dtype)
array = np.zeros(9, img.dtype)


for i in range(H):
    for j in range(W):
        num=0
        for mi in range(-1,2):
            for mj in range(-1,2):
                if(-1<i+mi<H) and (-1 < j + mj <W):
                    array[num]=img[i+mi,j+mj]
                    num +=1

        for si in range(num-1):
            for sj in range(num-1-si):
                if array[sj] > array[sj+1]:
                    array[sj], array[sj+1] = array[sj+1], array[sj]
        median[i,j] = array[4]



cv.imwrite("./median.bmp", median)
cv.imshow("median", median)
cv.waitKey(0)
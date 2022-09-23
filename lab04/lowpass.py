import cv2 as cv
import numpy as np

img = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("img", img)
H,W,C = img.shape[:]

l3 = np.zeros((H, W, C), img.dtype)
l5 = np.zeros((H, W, C), img.dtype)

array_3 = [[1/9 for col in range(3)] for row in range(3)]
array_5 = [[1/25 for col in range(5)] for row in range(5)]

for i in range(H):
    for j in range(W):
        valB = 0
        valG = 0
        valR = 0
        for mi in range(-1, 2):
            for mj in range(-1, 2):
                if (-1 < i+mi < H) and (-1 < j + mj < W):
                    valB = valB + img[i + mi, j + mj, 0] * array_3[mi + 1][mj + 1]
                    valG = valG + img[i + mi, j + mj, 1] * array_3[mi + 1][mj + 1]
                    valR = valR + img[i + mi, j + mj, 2] * array_3[mi + 1][mj + 1]
        l3[i ,j, 0] = np.rint(valB)
        l3[i, j, 1] = np.rint(valG)
        l3[i, j, 2] = np.rint(valR)

        valB = 0
        valG = 0
        valR = 0
        for mi in range(-2, 3):
            for mj in range(-2, 3):
                if (-2 < i+mi < H) and (-2 < j + mj < W):
                    valB = valB + img[i + mi, j + mj, 0] * array_5[mi + 2][mj + 2]
                    valG = valG + img[i + mi, j + mj, 1] * array_5[mi + 2][mj + 2]
                    valR = valR + img[i + mi, j + mj, 2] * array_5[mi + 2][mj + 2]
        l5[i, j, 0] = np.rint(valB)
        l5[i, j, 1] = np.rint(valG)
        l5[i, j, 2] = np.rint(valR)



cv.imwrite("./lowpass3.bmp", l3)
cv.imwrite("./lowpass5.bmp", l5)
cv.imshow("3*3", l3)
cv.imshow("5*5", l5)
cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("coin.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H, W = img.shape[:]
dil = np.zeros((H, W), img.dtype)
close = np.zeros((H, W), img.dtype)
array = np.zeros(81, img.dtype)
ero = np.zeros((H, W), img.dtype)



#최소값
def erosion(img1):
    for i in range(H):
        for j in range(W):
            min = 255
            count = 0
            for mi in range(-4, 5):
                for mj in range(-4, 5):
                    if (-1 < i + mi < H) and (-1 < j + mj < W):
                        array[count] = img1[i + mi, j + mj]
                        if array[count] <= min:
                            min = array[count]
                        count += 1
            ero[i, j] = min
    return ero


#최대값
def dilation(img1):
    for i in range(H):
        for j in range(W):
            max = 0
            count = 0
            for mi in range(-4, 5):
                for mj in range(-4, 5):
                    if (-1 < i + mi < H) and (-1 < j + mj < W):
                        array[count] = img1[i + mi, j + mj]
                        if array[count] >= max:
                            max = array[count]
                        count += 1
            dil[i, j] = max

    return dil


def closing():
    erosion(dil)
    for i in range(H):
        for j in range(W):
            close[i, j] = ero[i, j]

    return close


dilation(img)
cv.imwrite("dilation.bmp", dil)
cv.imshow("dilation", dil)
erosion(img)
cv.imwrite("erosion.bmp", ero)
cv.imshow("erosion", ero)
closing()
cv.imwrite("closing.bmp", close)
cv.imshow("closing", close)
cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread("rice.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H, W = img.shape[:]

dil = np.zeros((H, W), img.dtype)
ero = np.zeros((H, W), img.dtype)
top = np.zeros((H, W), img.dtype)
array = np.zeros(169, img.dtype)

#최소값
def erosion(img1):
    for i in range(H):
        for j in range(W):
            min = 255
            count = 0
            for mi in range(-6, 7):
                for mj in range(-6, 7):
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
            for mi in range(-6, 7):
                for mj in range(-6, 7):
                    if (-1 < i + mi < H) and (-1 < j + mj < W):
                        array[count] = img1[i + mi, j + mj]
                        if array[count] >= max:
                            max = array[count]
                        count += 1
            dil[i, j] = max
    return dil

eros = erosion(img)
dila = dilation(eros)

def tophat():
    for i in range(H):
        for j in range(W):
            top[i,j] = img[i,j]-dila[i,j]

    return top

top = tophat()


cv.imwrite("tophat.bmp", top)
cv.imshow("tophat", top)
cv.imwrite("dilation.bmp", dila)
cv.imshow("dilation", dila)
cv.waitKey(0)
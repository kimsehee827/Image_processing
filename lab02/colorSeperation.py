# lab02_colorSeparation into R, G, B
import cv2 as cv
import numpy as np

img = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("image", img)
H, W, C = img.shape[:]
img2 = np.zeros((H, W, C), img.dtype)
img3 = np.zeros((H, W, C), img.dtype)
img4 = np.zeros((H, W, C), img.dtype)


for y in range(H):
    for x in range(W):
        #for C in range(3):
        img2[y, x, 0] = img[y,x,0]
        img3[y, x, 1] = img[y,x,1]
        img4[y, x, 2] = img[y,x,2]

cv.imwrite('D:/mandrill2.bmp',img2)
cv.imwrite('D:/mandrill3.bmp',img3)
cv.imwrite('D:/mandrill4.bmp',img4)
cv.imshow("1816950_B", img2)
cv.imshow("1816950_G", img3)
cv.imshow("1816950_R", img4)
cv.waitKey(0)
import cv2 as cv
import numpy as np
import math

src = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("img", src)
H, W, C = src.shape[:]
output = np.zeros((2*H, 3*W, C), src.dtype)
ratioX = 3.0
ratioY = 2.0

for yd in range(H*int(ratioY)):
    for xd in range(W*int(ratioX)):
        xo = xd / ratioX
        yo = yd / ratioY

        xf = (xd // 3)
        yf = (yd // 2)

        xc = -(- xd // 3)
        yc = -(- yd // 2)

        a = xo - xf
        b = yo - yf

        if (xc < 256) and (yc < 256):
            output[yd, xd] = (1-a)*(1-b) * src[yf, xf] + a*(1-b) * src[yf, xc] + (1 - a) * b * src[yc, xf] + a*b * src[yc, xc]

cv.imwrite("geometric.bmp", output)
cv.imshow("geometric", output)
cv.waitKey(0)
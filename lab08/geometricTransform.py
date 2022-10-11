import cv2 as cv
import numpy as np

img = cv.imread("mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("img", img)
H, W, C = img.shape[:]
output = np.zeros((2*H, 3*W, C), img.dtype)
ratioX = 3.0
ratioY = 2.0

for yd in range(H*2):
    for xd in range(W*3):
        xo = xd / ratioX
        yo = yd / ratioY
        #내림
        xod = (xd // 3)
        yod = (yd // 2)
        # 올림
        xou = - (- xd // 3)
        you = - (- yd // 2)

        a = xo - xod
        b = yo - yod
        A = (1 - a) * (1 - b)
        B = a * (1 - b)
        C = (1 - a) * b
        D = a * b

        for c in range(3):
            if (xou < 256) and (you < 256):
                output[yd, xd, c] = A * img[yod, xod, c] + B * img[yod, xou, c] + C * img[you, xod, c] + D * img[
                    you, xou, c]
            else:
                output[yd, xd, c] = img[yod, xod, c]


cv.imwrite("geometric.bmp", output)
cv.imshow("geometric", output)
cv.waitKey(0)
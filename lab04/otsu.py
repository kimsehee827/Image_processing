import cv2 as cv
import numpy as np

img = cv.imread("coin.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H,W = img.shape[:]
otsu = np.zeros((H, W), img.dtype)
hist = np.zeros(256, float)
p = np.zeros(256,float)
q1 = np.zeros(256,float)
q2=np.zeros(256,float)
m1=np.zeros(256,float)
m2=np.zeros(256,float)
o1 = np.zeros(256,float)
o2 = np.zeros(256,float)
r = np.zeros(256,float)

#hist획득

for h in range(H):
    for w in range(W):
        hg = img[h,w]
        hist[hg] = hist[hg] + 1


#확률 구하기
for i in range(256):
    p[i] = hist[i]/(H*W)


for k in range(256):
    for i in range(k+1):
        q1[k] = p[i] + q1[k]
    for i in range(k+1,256):
        q2[k] = p[i] + q2[k]


    for i in range(k+1):
        if q1[k]:
            m1[k] = m1[k] + i * (p[i] / q1[k])
    for i in range(k+1,256):
        if q2[k]:
            m2[k] = m2[k] + i * (p[i] / q2[k])



    for i in range(k+1):
        if q1[k]:
            o1[k] = o1[k] + (i-m1[k])**2 * p[i] / q1[k]
    for i in range(k+1,256):
        if q2[k]:
            o2[k] = o2[k] + (i - m2[k]) ** 2 * p[i] / q2[k]


#find k
min = 0
for i in range(255):
    r[i] = m1[i] * o1[i] + m2[i] * o2[i]
    if r[i] < r[min]:
        min = i


for h in range(H):
    for w in range(W):
        if img[h,w] >= min:
            otsu[h,w] = 255
        else:
            otsu[h,w] = 0


cv.imwrite("./otsu.bmp", otsu)
cv.imshow("otsu", otsu)
cv.waitKey(0)
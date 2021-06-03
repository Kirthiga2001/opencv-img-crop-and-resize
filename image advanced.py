#crop and resize
import cv2
import numpy as np
i=cv2.imread("lena.jpg")
print(i.shape) #size of
ir=cv2.resize(i,(200,200)) #opencv- width and h
ic=i[0:200,200:500]  #h,w
cv2.imshow("original",i)
cv2.imshow("resize",ir)
cv2.imshow("crop",ic)

cv2.waitKey(0)
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('cats.jpg')
cv.imshow('cats',img)

blank=np.zeros(img.shape[:2], dtype='uint8')
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),150,(255,255,255),-1)
rectangle= cv.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),-1)

shape= cv.bitwise_and(circle,rectangle)
circle_masked= cv.bitwise_and(img,img,mask=circle)
rectangle_masked=cv.bitwise_and(img,img,mask=rectangle)
cv.imshow('circle masked',circle_masked)
cv.imshow('rectangle masked',rectangle_masked)

cv.waitKey(0)

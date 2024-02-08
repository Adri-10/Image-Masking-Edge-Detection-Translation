import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blank= np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle= cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_AND',bit_and)

bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_OR',bit_or)

bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_XOR',bit_xor)

circle_bit_not = cv.bitwise_not(rectangle,circle)
cv.imshow('circle bitwise_NOT',circle_bit_not)

cv.waitKey(0)




import cv2 as cv
import numpy as np
img = cv.imread('sudoku.jpg')
cv.imshow('sudoku', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('sudoku in gray', gray)

laplacian= cv.Laplacian(gray, cv.CV_64F,)
cv.imshow('sudoku in laplacian', laplacian)
lap= np.uint8(np.absolute(laplacian))
cv.imshow('sudoku in lap',lap)

sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined= cv.bitwise_or(sobelx,sobely)

cv. imshow('sobelx',sobelx)
cv. imshow('sobely',sobely)
cv. imshow('combined',combined)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
combined= np.uint8(np.absolute(cv.bitwise_or(sobelx,sobely)))

cv. imshow('sobel_x',sobelx)
cv. imshow('sobel_y',sobely)
cv. imshow('combined_d',combined)

cv.waitKey(0)



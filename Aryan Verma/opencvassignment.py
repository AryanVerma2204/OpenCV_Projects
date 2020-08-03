# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
font = cv.FONT_HERSHEY_SIMPLEX
imgo = cv.imread('sample2.png',-1)
img = imgo.copy()
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h=imgo.shape[0]
w=imgo.shape[1]


lower_w = np.array([0,0,0])
upper_w = np.array([0,0,255])

lower_r = np.array([0,50,50])
upper_r = np.array([10,255,255])

mask_w = cv.inRange(img_hsv, lower_w, upper_w)
mask_r = cv.inRange(img_hsv, lower_r, upper_r)


blur = cv.GaussianBlur(img,(5,5),0)
blur = cv.blur(blur,(5,5))
img_gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray,171,255,cv.THRESH_TOZERO)
canny = cv.Canny(thresh,180,255)
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

chips_contours = []
for i in range(len(contours)):
    if cv.contourArea(contours[i]) > 1250 :
        chips_contours.append(contours[i])
        
contours_final=[]
for i in range(len(chips_contours)):
      if i%2==0:
            contours_final.append(chips_contours[i])
          

for iter in range(len(contours_final)):
        temp = cv.imread('sample2.png',-1)
        temp_img = cv.cvtColor(temp,cv.COLOR_BGR2RGB) 
      
        
        moment = cv.moments(contours_final[iter])
        cx = int(moment['m10']/moment['m00'])
        cy= int(moment['m01']/moment['m00'])         
        cv.putText(imgo, 'Rejected', (cx, cy), font, 0.4, (0, 0, 255), 1, cv.LINE_AA)
     

cv.imwrite("answer.png",imgo)

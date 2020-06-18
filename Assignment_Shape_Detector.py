


import numpy as np
import cv2

font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.imread('A1.png')

def classifier(lower,upper):
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.imread('A1.png')

    mask= cv2.inRange(img,lower,upper)
    res= cv2.bitwise_and(img, img, mask = mask) 
    gray= cv2.blur(mask,(7,7)) 
    _,contours,hierarchy= cv2.findContours(gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        M= cv2.moments(c)
        posX= int((M["m10"] / M["m00"]))
        posY= int((M["m01"] / M["m00"]))
        area=cv2.contourArea(c)
        if area>100:
            approx = cv2.approxPolyDP(c, 0.03*cv2.arcLength(c, True), True)
            if len(approx) == 3:
                cv2.putText(mask, "Triangle", (posX-60,posY-60), font, 0.5, (255,255,255))
            elif len(approx) == 4:
                cv2.putText(mask, "Quadrilateral", (posX-60,posY-60), font, 0.5, (255,255,255))
            elif len(approx)==5:
                cv2.putText(mask, "Pentagon", (posX-60,posY-60), font, 0.5, (255,255,255))
            else:
                cv2.putText(mask, "Circle", (posX-60,posY-60), font, 0.5, (255,255,255))

    return mask;
color=['Red','Green','Blue','Yellow','Orange']
color_range = [([10,10,190],[100,100,255]),([20, 160, 20],[155, 255, 155]),([160,0,0],[255,200,100]),([10, 180, 180],[100, 255, 255]),([10, 130, 210],[120, 180, 255])]
index = 0
for (lower,upper) in color_range:
    masked = classifier(np.array(lower),np.array(upper))
    cv2.imshow("Original Image",img)
    cv2.imshow(f"{color[i]}coloured Objects",masked)
    i+=1
    cv2.waitKey(0)
    cv2.destroyAllWindows()







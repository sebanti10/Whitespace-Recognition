import numpy as np
import cv2

img = cv2.imread('12.png')
original = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

image = img.copy()

blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8,8))
dilate = cv2.dilate(thresh, kernel , iterations=3)


# Find contours in the image
cnts = cv2.findContours(dilate.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

contours = []

threshold_min_area = 90000
#threshold_max_area = 180000

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    area = cv2.contourArea(c)
    
    if area > threshold_min_area:
    	#print("area: "+ str(area))
    	#print("c: " + str(c) + "\nx,y,w,h")
    	#print(x,y,w,h)
    	#cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    	cv2.line(img, ((x+w)//2,y), ((x+w)//2,y+h), (0,255,0), 2)
    	#contours.append(c)

cv2.imwrite('result.png',img) 
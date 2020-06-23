# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:46:44 2020

@author: Avinash
"""

import numpy as np
import cv2

img = cv2.imread("OpenCV_Logo.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("number of contours: "+str(len(contours)))

cv2.drawContours(img, contours, -1, (255,255,0), 3)

cv2.imshow("image with contours:", img)
cv2.imshow("gray image", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
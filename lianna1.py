# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:17:06 2019

@author: AUTHOR NAME
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# set working directory
os.chdir("C:/Users/USER_ID_HERE/Documents/Colour_index/")

# print the name of the current working directory
print(os.getcwd())

# list files in wd
os.listdir()

# assign image to variable and show image
img = cv2.imread('IMG_6672_colour_calibration_ - Copy.JPG')
plt.imshow(img)

# set thresholds for image thresholding
hsv_lower = (0, 60, 40) # originally (30, 60, 60)
hsv_higher = (255, 255, 255)

# convert RGB to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)

# threshold image (this makes a black and white image)
hsv1 = cv2.inRange(hsv, hsv_lower, hsv_higher)
plt.imshow(hsv1)

dest = cv2.bitwise_and(img, img, mask = hsv1)
plt.imshow(dest)
    
# draw contours on image
contours, hierarchy = cv2.findContours(hsv1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt2 = cv2.drawContours(dest, contours, -1, (0, 0, 0), 4)
plt.imshow(cnt2)    
    
cv2.imwrite("thresh_img_test_8.JPG", cnt2)

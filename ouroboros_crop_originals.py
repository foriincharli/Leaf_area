# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:27:35 2019

@author: foriincharli
"""


import cv2
import numpy as np
import os
import csv
from datetime import datetime

root = "/Users/foriincharli/location/Expt Optimisation/Round plates - Shortlist/"
out = "/Users/foriincharli/location/Expt Optimisation/Crop by Python/"

hsv_lower = (32, 60, 60)
hsv_higher = (80, 255, 255)
shpfiles = []

for dirpath, subdirs, files in os.walk(root):
    shpfiles.extend(os.path.join(dirpath, x) for x in files if x.endswith(".jpg"))  

for i in range(len(files)):
    impath = root + '/' + files[i]
    img = cv2.imread(impath)
    img = img[200:5400, 600:3900]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.inRange(hsv, hsv_lower, hsv_higher)
    dest = cv2.bitwise_and(img, img, mask = hsv1)
    img2, contours, hierarchy = cv2.findContours(hsv1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt2 = cv2.drawContours(dest, contours, -1, (0, 255, 0), 4)
    newName = 'seg' + '_' + files[i] # remember to change the index if the file name changes! 
    cv2.imwrite(out + '/' + newName, cnt2)
    for i in range(len(contours)):
        BW = np.uint8(np.zeros((hsv1.shape)))
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area < 50: continue    
        # print(area)
        cv2.drawContours(BW, [cnt], 0, (255, 255, 255), -1)
        with open("threshed_round4.csv", 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([datetime.now(), newName, area])
    

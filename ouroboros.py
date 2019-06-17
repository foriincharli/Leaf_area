# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:41:51 2019

@author: cjfrancois
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# np.count_nonzero(hsv1) # for counting non-zero pixels

hsv_lower = (32, 60, 60)
hsv_higher = (80, 255, 255)

root = "C:/Users/cjfrancois/OneDrive - LA TROBE UNIVERSITY/myLTU/Python tutorial/pics"
out = "C:/Users/cjfrancois/OneDrive - LA TROBE UNIVERSITY/myLTU/Python tutorial/pics_output"
shpfiles = []
for dirpath, subdirs, files in os.walk(root):
    shpfiles.extend(os.path.join(dirpath, x) for x in files if x.endswith(".jpg"))

for i in range(len(files)):
    impath = root + '/' + files[i]
    img = cv2.imread(impath)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.inRange(hsv, hsv_lower, hsv_higher)
    dest = cv2.bitwise_and(img, img, mask = hsv1)
    contours, hierarchy = cv2.findContours(hsv1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt2 = cv2.drawContours(dest, contours, -1, (0, 255, 0), 4)
    newName = 'seg' + '_' + files[i].split('_')[2:][0] # remember to change the index if the file name changes! 
    cv2.imwrite(out + '/' + newName, cnt2)


for i in range(len(contours)):
    BW = np.uint8(np.zeros((hsv1.shape)))
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if area < 10: continue    
    print(area)
    cv2.drawContours(BW, [cnt], 0, (255, 255, 255), -1)
    plt.imshow(BW)
    plt.show()

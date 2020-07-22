# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:03:01 2020

@author: Nikitha
"""
import cv2
import numpy as np
import random
import os 

img=cv2.imread( 'C:\\Users\\Nikitha\\Desktop\\spyder\\New folder\\images.jpg',1)
cv2.namedWindow('oimg',cv2.WINDOW_NORMAL)
cv2.imshow('oimg',img)
cv2.waitKey(0)
h,w,n=img.shape
def sp_noise(img,prob):
    output=np.zeros(img.shape,np.uint8)
    thres=1-prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn=random.random()
            if rdn<prob:
                output[i][j]=0
            elif rdn >thres:
                output[i][j]=255
            else:
                output[i][j]=img[i][j]
    return output      

 
noise_img=sp_noise(img,0.01)
noise_img2=sp_noise(img,0.2)
noise_img3=sp_noise(img,0.09)

cv2.namedWindow('spimg',cv2.WINDOW_NORMAL)
cv2.imshow('spimg',noise_img)  

cv2.namedWindow('spimg2',cv2.WINDOW_NORMAL)
cv2.imshow('spimg2',noise_img2) 

cv2.namedWindow('spimg3',cv2.WINDOW_NORMAL)
cv2.imshow('spimg3',noise_img3) 

cv2.namedWindow('oimg',cv2.WINDOW_NORMAL)
cv2.imshow('oimg',img)



cv2.imwrite('saved_image1.jpg',noise_img)
cv2.imwrite('saved_image2.jpg',noise_img2)
cv2.imwrite('saved_image3.jpg',noise_img3)

cv2.waitKey(0)              
    







  
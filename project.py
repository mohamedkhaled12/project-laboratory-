from operator import invert
from turtle import width
import cv2 as cv
import numpy as np
# Reading videos
capture = cv.VideoCapture('Videos/water-PVP_0.mp4')
kernel = np.ones((5,5), np.int8)
#read the video frame by frame
#function to do the rotation
def roatate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        #roattion matrix
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width,height)

        return cv.warpAffine(img, rotMat, dimensions)    



while True:
    isTrue, frame = capture.read()
    # to find the edges
    imgcanny = cv.Canny(frame, 225, 100)
    rotated = roatate(imgcanny, 270)
    cv.imshow('Video', rotated)
#to prevent the video from being read indefinetly 
#if letter d is pressed break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
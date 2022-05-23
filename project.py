from pickle import TRUE
from re import X
from tabnanny import check
import cv2 as cv
import numpy as np

# Reading videos
capture = cv.VideoCapture('Videos/water-PVP_0.mp4')
isTrue, frame = capture.read()

frame_count = capture.get(cv.CAP_PROP_FRAME_COUNT)
width  = capture.get(3)  # float `width
height = capture.get(4)  # float `height`
print(width, ' ', height)
# print(frame_count)
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


(chk_point_x, chk_point_y) = (1, 1)
count = 0
if count ==0:
    def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
       if event == cv.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
         chk_point_x = x
         chk_point_y = y
         print(chk_point_x, ' ', chk_point_y)

    blur = cv.GaussianBlur(frame, (5,5), 0)
    imgcanny = cv.Canny(blur, 115, 342)
    rotated = roatate(imgcanny, 270)
     #finding the contours
    contours, hierarchy = cv.findContours(rotated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    
    #drawing contours
    drawing = np.zeros((rotated.shape[0], rotated.shape[1], 3), dtype=np.uint8)

    for i in range(len(contours)):
        cv.drawContours(drawing, contours, i, (255,255,255), 3)

    for cnt in contours:
        area = cv.contourArea(cnt)
        peri = cv.arcLength(cnt, True)
        # x, y, w, h = cv.boundingRect(approx)
        # cv.rectangle(drawing, (x, y), (x + w, y + h ), (0, 255, 0), 5)
        cv.putText(drawing, "Perimeter: " + str(int(peri)), (40, 40), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)
        cv.putText(drawing, "Area: " + str(int(area)),(20, 20), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

        ellipse = cv.fitEllipse(cnt)
        cv.ellipse(drawing,ellipse,(0,255,0),2)
    cv.imshow('Video', drawing)
    cv.namedWindow('Video')
    cv.imshow('Video', drawing)
    cv.setMouseCallback('Video', click_event)
    cv.waitKey()


distances= []
count+=1
while isTrue:
    key = cv.waitKey(20)
    
    def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
       if event == cv.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
         chk_point_x = x
         chk_point_y = y
         print(chk_point_x, ' ', chk_point_y)
        
       
    blur = cv.GaussianBlur(frame, (5,5), cv.BORDER_DEFAULT)
    imgcanny = cv.Canny(blur, 115, 342)
    rotated = roatate(imgcanny, 270)
     #finding the contours
    contours, hierarchy = cv.findContours(rotated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #drawing contours
    drawing = np.zeros((rotated.shape[0], rotated.shape[1], 3), dtype=np.uint8)
    contours_length = len(contours)
    
    for i in range(len(contours)):
        cv.drawContours(drawing, contours, i, (255,255,255), 3 )
     
    for cnt in contours:
        area = cv.contourArea(cnt)
        peri = cv.arcLength(cnt, True)
        ellipse = cv.fitEllipse(cnt)
        cv.ellipse(drawing,ellipse,(0,255,0),2)
        cv.putText(drawing, "Area: " + str(int(area)),(20, 20), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)
        cv.putText(drawing, "Perimeter: " + str(int(peri)), (40, 40), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

    (check_x, check_y) = (height,width//2) 
    M = cv.moments(contours[contours_length-1])
    cX = int(M['m10'] /M['m00'])
    cY = int(M['m01'] /M['m00'])
    dx= cX - check_x
    dy = cY - check_y 
    D = np.sqrt(dx * dx + dy * dy)
    distances.append(D)
    
    if D <= 215:
        print('Detachemnt')
        print(D)
        cv.putText(drawing, "Detachmet",(60, 60), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
        
    else:
        print('Development') 
        print(D)
        cv.putText(drawing, "Development",(60, 60), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)   
  
    print(len(contours))       
    cv.imshow('Video', drawing)
    cv.namedWindow('Video')
    cv.imshow('Video', drawing)
    cv.setMouseCallback('Video', click_event)
 
     
    if key==32:
        cv.waitKey()

    elif key==ord('c'):
       cv.imshow('Video', drawing)
       cv.namedWindow('Video')
       cv.imshow('Video', drawing)
       cv.setMouseCallback('Video', click_event)

    
    #read next frame     
    isTrue, frame = capture.read()
    
#to prevent the video from being read indefinetly 
#if letter d is pressed break
    if key==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

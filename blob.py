import cv2
import numpy as np;
import sys
#beginnings of serial dilution chip code

######
#will add part to process image after have image

#from alex's code it seems he just tried a bunch of things until
#he found something that worked. i can research some general things
#though

#####

#for now just checking @ which well it stops fluorescing and error checks


#getting the image
im = cv2.imread("case1.jpeg", cv2.IMREAD_GRAYSCALE)

#params simple for now, will make more exact once have working images
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = False

#using cv2 library to find keypoints on image
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(im)
num = len(keypoints)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


#will change later, based on image
DISTANCE_FROM_EDGE_TO_FIRST_WELL = 55

#initializing arrays
distanceArray = []
initialArray = []

#making an array of just x values(bc only one row)
for i in range(0, num):
   initialArray.append(keypoints[i].pt[0])

#sorting array so in order of well(L to R)
initialArray = sorted(initialArray)

#to find distance between wells/btwn wells and origin
initial = 0
for i in range (0, num):
   if i != 0:
      initial = initialArray[i - 1]
      
   distanceArray.append(initialArray[i] - initial)

   #if some error happened and have wells fluorescing wrong
   #will fine tune parameters once working with actual images
   if i == 0:
      if distanceArray[0] >= DISTANCE_FROM_EDGE_TO_FIRST_WELL:
         print 'Error code 1!!'
         sys.exit()
   if i != 0:
      if distanceArray[i] >= ((keypoints[i].size)*2) + 1 :
         print 'Error code 2!'
         sys.exit()


#otherwise this is the well it stops fluroescing at
print num
 

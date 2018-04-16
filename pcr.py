import cv2
import numpy as np;
import sys
#getting the image


im = cv2.imread('pcr.jpg', cv2.IMREAD_GRAYSCALE)

#denoising image
denoised_img = cv2.fastNlMeansDenoising(im, None, 9, 40)


#params to find fluroescing well
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = False
params.filterByArea = True
params.minArea = 50
minDistBetweenBlobs = 50;

#using cv2 library to find keypoints on image
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(denoised_img)
num = len(keypoints)
im_with_keypoints = cv2.drawKeypoints(denoised_img, keypoints, np.array([]), (0, 0, 255),
cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('im', im_with_keypoints)
cv2.waitKey(0)



#otherwise this is the well it stops fluroescing at
print num
 

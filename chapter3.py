import cv2 as cv

## Image reading Code, uncomment it for execution
#img = cv.imread("Resources/python.png") ##reading image from Resource path
#cv.imshow("Output", img) #showing output in window panel

#cv.waitKey(0) #waiting unlimitedly , if you give waitKey(1) means 1 millisecond

##Video reading Code , uncomment it for execution

#videoCap = cv.VideoCapture("Resources/videpath") ## video path need to mention

#while True:
 #   success, img = videoCap.read()
 #   cv.imshow("Video Output", img)

  #  if cv.waitKey(1) & 0xFF == ord('q'):
  #       break

### Webcam reading codes , uncomment it for execution

#videoCap = cv.VideoCapture(0) ## 0 is default web cam, you can change 1 or 2 based on the number of webcam, it represents webcam id.
#videoCap.set(3, 640)  ##Width of the Video
#videoCap.set(4, 480) ## Height of the Video
#videoCap.set(10, 100) ## Brightness adjustment

#while True:
 #   success, img = videoCap.read()
 #   cv.imshow("Video Output", img)

  #  if cv.waitKey(1) & 0xFF == ord('q'):
  #       break
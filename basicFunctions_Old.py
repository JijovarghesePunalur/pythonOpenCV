import cv2 as cv
import numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv.imread("Resources/python.png")
#cv.imshow("Normal Image Outout", img)


#Lets Print GrayScale Image

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("GrayScale Image", imgGray)

#Lets Print Blur Function - Gaussian Blur

imgBlur = cv.GaussianBlur(img, (5,7), 500)
#cv.imshow("Blur Image", imgBlur)

#Lets Print Canny Image

imgCanny = cv.Canny(img, 150, 200)
#cv.imshow("Canny Image", imgCanny)

#lets print image dilation.

imgDialation = cv.dilate(imgCanny, kernel, iterations=1)
#cv.imshow("Dialation", imgDialation)

#lets print erosion on dilated image

imgEroded = cv.erode(imgDialation, kernel, iterations=1)
#cv.imshow("Eroded Image", imgEroded)

#cv.waitKey(0)

### Applying Basic Functions on Videos.

videoCap = cv.VideoCapture("Resources/PUBG - Season 4 - Erangel Orchestra.webm") ## video path need to mention

while True:
    success, img = videoCap.read()
    #imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Grayscale
#    imgBlur = cv.GaussianBlur(img, (7, 7), 1000) #Blur
    imgCanny = cv.Canny(img, 100, 100) # Canny Image
    imgDialation = cv.dilate(imgCanny, kernel, iterations=3) #dilatation
    imgEroded = cv.erode(imgDialation, kernel, iterations=1) #erosion
    cv.imshow("Video Output", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
         break


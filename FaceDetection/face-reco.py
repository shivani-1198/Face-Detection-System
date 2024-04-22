import cv2

# imporing the test data
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# starting the webcam
webcam = cv2.VideoCapture(0)

while True:
    #  taking img from the video captured
    _, img = webcam.read() 
    
    # converting the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 4)
    # x, y, w, h refer to al the corner of the image
    for (x,y,w,h) in faces:
        #giving all the details to create the square: the image, height dimesnsion, the breath dimensions, the color of the rectangle line and the thicknes of it
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0),3)
    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10) #asking cv2 to wait 10 milisec for any key

    if key ==27: # assign the escape as the stop key
        break


# to close the webcamp when the escape is hit
webcam.release()
cv2.destroyAllWindows()

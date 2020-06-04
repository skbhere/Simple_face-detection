import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
# img = cv2.imread('gp.png')
cap = cv2.VideoCapture('facedetect.mp4')
out  =  cv2.VideoWriter('output.mp4',-1,20.0,(768,432))
if (cap.isOpened() == False):
    print("Error opening video  file")

# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray,1.1,4)
        for(x,y,w,h) in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(2500))
        #Display the resulting frame
        out.write(frame)
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()

##################################################
#same code for images

# #img = cv2.resize(img1,(0,0), fx=0.5, fy=0.5)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# for(x,y,w,h) in faces :
#     cv2.rectangle(img,(x,y),(x+w,y+h),(2500))
# cv2.imshow("Results",img)
# cv2.waitKey(0)
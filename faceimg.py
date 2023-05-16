import cv2
tr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('sky.png')
gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_dim=tr.detectMultiScale(gr)
(x,y,w,h)=face_dim[0]
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)
cv2.imshow('siva face detect app',img)
cv2.waitKey()
import cv2
import label_image

size = 4

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
webcam = cv2.VideoCapture(0)




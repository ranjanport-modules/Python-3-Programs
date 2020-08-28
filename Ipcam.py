import cv2
import numpy as np
url = "192.168.43.3/video"
MainUrl = str(url)
cap = cv2.VideoCapture(MainUrl)
while (True):
	ret, frame = cap.read()
	if frame is not None:
		cv2.imshow('frame',frame)
	q = cv2.waitKey(1)
	if q == ord ("q"):
		break
		cv2.destroyAllWindows()

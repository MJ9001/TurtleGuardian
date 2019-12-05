# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def nothing(x):
	pass
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
total_hue = 0
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array 
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
	# show the frame
	cv2.imshow("Frame", mask)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	for x in range(0,  639):
		for y in range(0, 479):
			total_hue += hsv[y][x][0]
	total_hue = total_hue / (640*480)
	print("Yellow val: " + str(total_hue) + "\n")
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

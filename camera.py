# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
cam = PiCamera()
cam.resolution = (640, 480)
cam.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the cui8iamera to warmup
class Camera:
    def __init__(self):
        
        
    def isMovement():
        
    # capture frames from the camera
    def runCamera:
        for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
         
            # show the frame
            cv2.imshow("Frame", image)
         
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
         

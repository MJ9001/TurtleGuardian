# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading 
import argparse
import imutils
# allow the cui8iamera to warmup
class Camera:
    # initialize the camera and grab a reference to the raw camera capture
    cam = PiCamera()
    cam.resolution = (640, 480)
    cam.framerate = 32
    rawCapture = PiRGBArray(cam, size=(640, 480))
    finish = False
    imageReading = False
    runDone = False
    
    def getImage(self):
        while True:
            self.imageReading = True
            while(self.runDone == False):
                pass
            print("Starting read image")
            time.sleep(0.1)
            fgbg = cv2.createBackgroundSubtractorMOG2()
            for frame in self.cam.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
                # grab the raw NumPy array representing the image, then initialize the timestamp
                # and occupied/unoccupied text
                image = frame.array
                mask = fgbg.apply(image)
                
                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                print("I found {} changes".format(len(cnts)))
                for c in cnts:
                    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                # show the frame
                cv2.imshow("Frame", image)
                key = cv2.waitKey(1) & 0xFF
                # clear the stream in preparation for the next frame
                self.rawCapture.truncate(0)

    def exit(self):
        self.finish = True
        
    def isMovement(self):
        pass
        
    # capture frames from the camera
    def runCamera(self):
        self.runDone = False
        for frame in self.cam.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            self.imgGet = image
            # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)
            if self.finish or self.imageReading:
                print("Exiting camera module")
                self.runDone = True
                break
         
    def __init__(self):
        x = threading.Thread(target=self.runCamera)
        x.start()
        print("Camera module initalized")


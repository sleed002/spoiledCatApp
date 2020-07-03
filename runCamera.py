import picamera     # Importing the library for camera module
from time import sleep
camera = picamera.PiCamera()    # Setting up the camera
camera.capture('/home/pi/Desktop/spoiledCatApp/Milo.jpg') # Capturing the image
print('Done')


import picamera # Importing the library for camera module
import cloudinary
from cloudinary import uploader
from cloudinary import CloudinaryImage
import os
from configparser import ConfigParser

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configPath = os.path.join(basepath, "spoiledCatApp/etc", "config.ini")
config = ConfigParser()
config.read(configPath)

assert os.path.exists(configPath)

APIKEY = config.get("cloud", "APIKEY")
APISECRET = config.get("cloud", "APISECRET")
CLOUD_NAME = config.get("cloud", "CLOUD_NAME")

cloudinary.config(
  cloud_name = CLOUD_NAME,
  api_key = APIKEY,
  api_secret = APISECRET
);

from time import sleep
camera = picamera.PiCamera()
camera.rotation = 180 # Setting up the camera
camera.capture('/home/pi/Desktop/spoiledCatApp/Milo.jpg')
# Capturing the image
cloudinary.uploader.upload("/home/pi/Desktop/spoiledCatApp/Milo.jpg", use_filename="true", unique_filename="false",
                           invalidate="true")
print('Done')
  
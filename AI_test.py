from inference_sdk import InferenceHTTPClient 
from PIL import Image
from gpiozero import Robot
import RPi.GPIO as GPIO
import time
import cv2

#stuff for th motors
left = Robot((20,16), (6,5))  #front then back
right = Robot((13,19), (27,17))   #front then back

#stuff for e camera
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

#stuff for the LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#    set the led as on when the code strts
GPIO.output(18,GPIO.HIGH)

# stuff for the AI 
CLIENT = InferenceHTTPClient(
    api_url = "https://detect.roboflow.com", #idk if this is the correct website
    api_key = "_____" 
)

def cameraRead():
    #only take an image
    ret, frame = cam.read()
    print('camera working')
    #image = cv2.resize(frame, (320, 240))		
    #cv2.imshow('image', frame)
    cam.release()

    img_convert = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    PIL_image = Image.fromarray(img_convert)
    AI_model = "battlebot-detection-2.0-akvzk/1"

    outcomes = (CLIENT.infer(PIL_image, AI_model))
    print(outcomes)

    for predictions in outcomes['predictions']:
        obj_detected = predictions['class']

    print(obj_detected)

    #classed = print(outcomes["class"])
    #print(classed)
    #cv2.imshow('image', frame)

    howMove(obj_detected) #has the predicton and then sends the data to ht how move - send the class things to the function o be able to be analysed
    time.sleep(0.5)

def forwards():
    left.forward()
    right.forward()
    print('moving forward')

def backwards():
    left.backward()
    right.backward()
    print('moving backwards')

def turnLeft():
    left.backward()
    right.forward()
    print('movng left')

def turnRight():
    left.forward()
    right.backward()
    print('moving right')

def howMove(obj):
    #put stuff neededin here
    if obj == 'bag':
        turnLeft()
    elif obj == 'box':
        forwards()
    elif obj == 'chair':
        turnRight()
    elif obj == 'foot':
        turnLeft()
    elif obj == 'wall':
        backwards()     
    else:
        forwards()
    #want the thingy to check the class and thn call th functions depending on he outcome


while True:
    cameraRead() #this is hte only thing I plan to put in here 

#trying to get the classes working to do things based off the image shown (not camera)
from inference_sdk import InferenceHTTPClient 
from gpiozero import Robot
import time

left = Robot((20,16), (6,5))  #front then back
right = Robot((13,19), (27,17))   #front then back


CLIENT = InferenceHTTPClient(
    api_url = "https://detect.roboflow.com", #idk if this is the correct website
    api_key = "______" # figure out what my api key is and put it in there 
)

result = CLIENT.infer(
    "/home/evelvevl/battlebot/chair2.jpeg", # test images put here 
    model_id = "battlebot-detection-2.0-akvzk/1" # my AI thingy 
    )

for predictions in result['predictions']:
    classed = predictions['class']
     #maybe add in an if tatement to see if it resturn a string and if nt set the string as null s
print(classed)

def forwards():
    left.forward()
    right.forward()
    print('moving forwards')

def backwards():
    left.backward()
    right.backward()
    print('moving backwards')

def turnLeft():
    left.backward()
    right.forward()
    print('turning left')

def turnRight():
    left.forward()
    right.backward()
    print('tuning right')

def howMove():
    #put stuff neededin here
    print("moving")


#this is he if stateent that will be used to determine the battlebot movement
if classed == 'bag':
    turnLeft()
elif classed == 'box':
    forwards()
elif classed == 'chair':
    turnRight()
elif classed == 'foot':
    turnLeft()
elif classed == 'wall':
    backwards() 
else:
    forwards() 

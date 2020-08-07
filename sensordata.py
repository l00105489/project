import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Pir = 17
GPIO.setup(Pir,GPIO.IN)

Mat = 4
GPIO.setup(Mat,GPIO.IN)

Mic = 26
GPIO.setup(Mic, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def pirSensor():
      if GPIO.input(Pir):
          #print ("Motion Detected")
          return 1
      else:
          #print ("Motion Not Detected")
          return 0

def matSensor():
    prev_input = 0
    input = GPIO.input(Mat)
    if ((not prev_input) and input):
        #print("Under Pressure")
        return 1
    else:
        #print ("No Pressure")
        return 0
    prev_input = input

def micSensor():
    if GPIO.input(Mic)==GPIO.HIGH:
            #print ("Sound Detected!")
            time.sleep(0.5)
            return 1
    else:
            #print ("Sound Not Detected")
            return 0
#         
# try:
#     while True:
#         sensor1=pirSensor()
#         sensor2=matSensor()
#         sensor3=micSensor()
#         print ("PIR", sensor1, "MAT", sensor2,"MIC", sensor3)
#         #print ("PIR", sensor1)
#         time.sleep(0.10)
# except KeyboardInterrupt:
#     pass
# finally:
#     GPIO.cleanup()

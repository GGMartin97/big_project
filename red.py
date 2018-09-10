import RPi.GPIO as GPIO
import time
import picamera

camera=picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN)
camera.resolution=(2592,1944)
camera.rotation=180
def work():
    timeString=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if GPIO.input(13):
        print('noting')
    else:
        camera.capture(timeString+'.jpg')
        print('successed')

if __name__=='__main__':
    while True: 
        work()
        time.sleep(3)

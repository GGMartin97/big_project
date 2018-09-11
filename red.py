import RPi.GPIO as GPIO
import time
import picamera
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

time.sleep(1)
mail_host="smtp.qq.com"  
mail_user="759224761@qq.com"
mail_pass="iirdocuhfvznbdcj"   

sender = '759224761@qq.com'
receivers = ['martinofcode@gmail.com']  

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
        message = MIMEMultipart()
        message['From'] = Header("306", 'utf-8')
        message['To'] =Header("test", 'utf-8')
        subject = '306 yyyy'
        message['Subject'] = Header(subject, 'utf-8')
         
        message.attach(MIMEText('hello world', 'plain', 'utf-8'))
         
        att1 = MIMEImage(open(timeString+'.jpg', 'rb').read())
        att1.add_header('Content-ID','image.jpg')
        message.attach(att1)
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("success")
        except smtplib.SMTPException:
            print ("Error:")
        print('successed')

if __name__=='__main__':
    while True: 
        work()
        time.sleep(3)

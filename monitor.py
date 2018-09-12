from BMP180 import BMP180
import time
import sqlite3
import RPi.GPIO as GPIO
import picamera
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

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
bmp=BMP180()


def getdate():
    conn=sqlite3.connect('temp.db')
    c=conn.cursor()
    temp=bmp.read_temperature()
    pressure=bmp.read_pressure()
    pressure=pressure/100
    t=int(time.time())
    c.execute("INSERT INTO HOMEDATE VALUES(?,?,?)",(temp,pressure,t))
    conn.commit()
    conn.close()
    print('ok')

def alarm_system():
    timeString=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if GPIO.input(13):
        print('noting')
    else:
        camera.capture(timeString+'.jpg')
        message = MIMEMultipart('related')
        message['From'] = Header("759224761@qq.com", 'utf-8')
        message['To'] =Header("martinofcode@gmail.com", 'utf-8')
        subject = '306 yyyy'
        message['Subject'] = Header(subject, 'utf-8')
        
        msgAlternative=MIMEMultipart('alternative')
        message.attach(msgAlternative)
        mail_msg="""
        <p>python test </p>
        <p><img src="cid:image1"</p>
        """
        msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))
        atemp=timeString+'.jpg'
        att1 = MIMEImage(open(atemp, 'rb').read())
        att1.add_header('Content-ID','<image1>')
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
        time.sleep(3)
        work()
        alarm_system()
        

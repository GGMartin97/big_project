from BMP180 import BMP180
import time
import sqlite3
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

while True:
    time.sleep(1)
    getdate()

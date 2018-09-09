from BMP180 import BMP180
import time
import sqlite3
bmp=BMP180()


def getdate():
    conn=sqlite3.connect('temp.db')
    c=conn.cursor()
    temp=bmp.read_temperature()
    t=int(time.time())
    c.execute("INSERT INTO BMP180 VALUES(?,?)",(temp,t))
    conn.commit()
    conn.close()
    print('ok')

while True:
    time.sleep(1)
    getdate()

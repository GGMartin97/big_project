from BMP180 import BMP180
import time
import sqlite3



bmp=BMP180()

while True:
    conn=sqlite3.connect('DATE.db')
    c=conn.cursor()

    temp=bmp.read_temperature()

    pressure=bmp.read_pressure()
    pressure=pressure/100

    altitude=bmp.read_altitude()

    timenow=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(timenow)
    
    c.execute("INSERT INTO HOMETEMP VALUES (?,?,?,?)",(timenow,temp,pressure,altitude))
    print("Records created successfully")
    c.close()
    conn.commit()
    conn.close()
    time.sleep(30)

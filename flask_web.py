import sqlite3
import json
from flask import Flask,request,render_template
import time

app=Flask(__name__)
tmp_time=0
tmp_time1=0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    global tmp_time
    conn1=sqlite3.connect('temp.db',check_same_thread=False)
    c1=conn1.cursor()
    if tmp_time>0:
        c1.execute('select * from HOMEDATE where TIME>?',((tmp_time/1000),))
    else:
        c1.execute('select * from HOMEDATE')
    arr=[]
    for i in c1.fetchall():
        arr.append([i[2]*1000,i[0]])
    if len(arr)>0:
        tmp_time=arr[-1][0]
    c1.close()
    conn1.close()
    return json.dumps(arr)
@app.route('/data1')
def data1():
    global tmp_time1
    conn2=sqlite3.connect('temp.db',check_same_thread=False)
    c2=conn2.cursor()
    if tmp_time1>0:
        c2.execute('select * from HOMEDATE where TIME>?',((tmp_time1/1000),))
    else:
        c2.execute('select * from HOMEDATE')
    arr2=[]
    for i in c2.fetchall():
        arr2.append([i[2]*1000,i[1]])
    if len(arr2)>0:
        tmp_time1=arr2[-1][0]
    c2.close()
    conn2.close()
    return json.dumps(arr2)
        
@app.route('/data3')
def data3():
    tmp_time3=int(time.time()-10)
    conn3=sqlite3.connect('temp.db',check_same_thread=False)
    c3=conn3.cursor()
    c3.execute('select * from HOMEDATE where TIME>?',(tmp_time3,))
    arr3=[]
    for i in c3.fetchall():
        arr3.append(i[0])
    if len(arr3)>0:
        return json.dumps(arr3[0])
    else:
        return json.dumps(100)





if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
    



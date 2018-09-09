import sqlite3
import json
from flask import Flask,request,render_template

app=Flask(__name__)
conn1=sqlite3.connect('temp.db',check_same_thread=False)
c1=conn1.cursor()
tmp_time=0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    global tmp_time
    conn1=sqlite3.connect('temp.db',check_same_thread=False)
    c1=conn1.cursor()
    if tmp_time>0:
        c1.execute('select * from BMP180 where TIME>?',((tmp_time/1000),))
    else:
        c1.execute('select * from BMP180')
    arr=[]
    for i in c1.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time=arr[-1][0]
    c1.close()
    conn1.close()
    return json.dumps(arr)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
    



import sqlite3
import json
from flask import Flask,request,render_template

app=Flask(__name__)
conn1=sqlite3.connect('temp.db',check_same_thread=False)
c1=conn1.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    sql='select * from BMP180'
    c1.execute(sql)
    arr=[]
    for i in c1.fetchall():
        arr.append([i[1]*1000,i[0]])
    return json.dumps(arr)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
    



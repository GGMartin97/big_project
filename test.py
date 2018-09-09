import sqlite3


tmp_time=0
tmp_time1=0
while True:
    conn=sqlite3.connect('temp.db',check_same_thread=False)
    c=conn.cursor()
    if tmp_time>0:
        c.execute('select * from BMP180 where TIME>?',('tmp_time/1000',))
    else:
        c.execute('select * from BMP180')
    arr=[]
    for i in c.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time=arr[-1][0]
    print(tmp_time)
    print(type(tmp_time))
    print('\n')
    print(arr)
    print('\n')
    if tmp_time==tmp_time1:
        break
    tmp_time1=tmp_time
    c.close()
    conn.close()

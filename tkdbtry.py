from tkinter import *
from PIL import ImageTk,Image
import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='joseph'
    )
top=Tk()
a=StringVar()
b=StringVar()
c=StringVar()
def getvalue():
   
    r=a.get()
    i=b.get()
    o=c.get()
    try:
        with connection.cursor() as cursor:
            sql=("""INSERT INTO just (name,email,password) VALUES ("%s","%s","%s")"""%(r,i,o))
            try:
                cursor.execute(sql)
                print("task added successfully")
            except:
                print("OOPs!, something went wrong")
        connection.commit()
    finally:
        connection.close()

top.geometry('400x250')
top.config(bg='light blue')


name = Label(top, text="Name",background="red").place(x=30,y=50)
email = Label(top, text="Email",background="red").place(x=30,y=90)
password = Label(top, text="Password",background="red").place(x=30,y=130)
sbmitbtn=Button(top,text="SUBMIT",activebackground="pink",command=getvalue).place(x=30,y=170)
e1=Entry(top,textvariable=a).place(x=100,y=50)
e2=Entry(top,textvariable=b).place(x=100,y=90)
e3=Entry(top,textvariable=c).place(x=100,y=130)
top.mainloop()

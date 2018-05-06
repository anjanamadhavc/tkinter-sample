from tkinter import *
from tkinter import messagebox
import sqlite3
def gendersel():
    selection="you selected "+Radiovar.get()
    L5.config(text=selection)

def checksel():
    sel=" "
    for (k,v) in zip(list(options.keys()),list(options.values())):
        if v.get()==1:
            sel+=k+","
    L6.config(text="you selected "+sel.strip())

def spinage():
    L8.config(text="your age is "+str(age.get()))
def signup(frame):
    print("signup")
    sel=" "
    for (k,v) in zip(list(options.keys()),list(options.values())):
        if v.get()==1:
            sel+=k+","
    conn=sqlite3.connect("test.db")
    sql_cmd="insert into user(name,password,hobbies,gender,age) values('"+name.get()+"','"+psw.get()+"','"+sel.strip()+"','"+Radiovar.get()+"',"+str(age.get())+");"
    print(sql_cmd)
    conn.execute(sql_cmd)
    print("inserted succesfully")
    conn.commit()
    conn.close()
    f2.tkraise()

def show():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    sql_cmd=("select * from user;")
    cursor.execute(sql_cmd)
    rows=cursor.fetchall()
    for row in rows:
        print("USER ID=",row[0])
        print("NAME=",row[1])
        print("PASSWORD=",row[2])
        print("HOBBIES=",row[3])
        print("GENDER=",row[4])
        print("AGE=",row[5])
    print("selected")
    conn.close()

top=Tk()
f2=Frame(top)
top.geometry("550x500")

name=StringVar()
psw=StringVar()

Checkvar1=IntVar()
Checkvar2=IntVar()
Checkvar3=IntVar()
Checkvar4=IntVar()

Radiovar=StringVar(value="Male")
options={"gardening":Checkvar1,"coding":Checkvar2,"swimming":Checkvar3,"reading":Checkvar4}

L1=Label(top,text="name").grid(row=0,column=0,sticky=W)
E1=Entry(top,textvariable=name,bd=5).grid(row=0,column=1,sticky=E)

L2=Label(top,text="password").grid(row=1,column=0,sticky=W)
E2=Entry(top,textvariable=psw,bd=5,show="*").grid(row=1,column=1,sticky=E)

L3=Label(top,text="your hobbies:").grid(row=3,column=0,sticky=W)
L6=Label(top)
L6.grid(row=3,column=2,sticky=E,columnspan=3)

c1=Checkbutton(top,text="gardening",
               command=checksel,
               variable=Checkvar1,
               onvalue=1,
               offvalue=0).grid(row=4,column=0,sticky=W)

c2=Checkbutton(top,text="coding",
               command=checksel,
               variable=Checkvar2,
               onvalue=1,
               offvalue=0).grid(row=5,column=0,sticky=W)

c3=Checkbutton(top,text="swimming",
               command=checksel,
               variable=Checkvar3,
               onvalue=1,
               offvalue=0).grid(row=6,column=0,sticky=W)


c4=Checkbutton(top,text="reading",
               command=checksel,
               variable=Checkvar4,
               onvalue=1,
               offvalue=0).grid(row=7,column=0,sticky=W)

L4=Label(top,text="gender:").grid(row=8,column=0,sticky=E)
R1=Radiobutton(top,text="Male",variable=Radiovar,value="male",command=gendersel).grid(row=8,column=1,sticky=W,columnspan=3)
R2=Radiobutton(top,text="Female",variable=Radiovar,value="female",command=gendersel).grid(row=8,column=2,sticky=W,columnspan=3)
R3=Radiobutton(top,text="Other",variable=Radiovar,value="other",command=gendersel).grid(row=8,column=3,sticky=W,columnspan=3)

L5=Label(top)
L5.grid(row=9,column=3,sticky=E)

L7=Label(top,text="age:").grid(row=10,column=0,sticky=W)
age=Spinbox(top,from_=15,to=75,command=spinage)
age.grid(row=10,column=1)

L8=Label(top)
L8.grid(row=10,column=3,sticky=E)

B1=Button(top,text="signup",command=signup(f2))
B1.grid(row=11,column=1)

B2=Button(top,text="show user details",command=show)
B2.grid(row=11,column=2)

for i in range(0,5):
    top.grid_columnconfigure(i,weight=1,uniform="group1")

for i in range(0,10):
    top.grid_rowconfigure(i,weight=1,uniform="group1")

top.mainloop()

from tkinter import *
#from Tkinter.font import Font
import os
root=Tk()
root.title("Energy Production Manager")
count=0


def reset(event):
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    l3.grid(row=2,sticky=W)
    e6.grid(row=2,column=1)
    
def display(event):
    data=open('data.txt','r')
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split()
        j+=1
        data_list.append(l)
   
    global count
    if count<=len(data_list)-1:
        s1.set(data_list[count][0])
        s2.set(data_list[count][1])
        s3.set(data_list[count][2])
        s4.set(data_list[count][3])
        s5.set(data_list[count][4])
        count+=1
        data.close()
    else:
        count=0
def record_added():
    l8=Label(root,text='Record Added')
    l8.grid(row=20,columns=3)

def updated():
    l8=Label(root,text='Record Updated')
    l8.grid(row=20,columns=3)
def data_error():
    l8=Label(root,text='INCORRECT Data')
    l8.grid(row=20,columns=3)
def add(event):
    data=open('data.txt','a+')
    name=s1.get()
    rm_tp=s2.get()
    ck_in=s3.get()
    ck_out=s4.get()
    num=s5.get()
    data.writelines(name+"  "+rm_tp+" "+ck_in+" "+ck_out+" "+" "+num+" "+'\n')
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    record_added()
    data.close()
#Search a record##########################################
def ok(event):
    import re
    flag=1
    data=open('data.txt','r')
    line=data.readlines()
    name=s6.get()
    for i in line:
        j = i.split()

        if(name==j[0]):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
            flag=1
            break
        else:
            flag=0
            pass
    if flag==0:
        s1.set('**No record Found**')
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
    data.close()
def delete(event):
    data=open('data.txt','r')
    s = s6.get()
    s6.set("")
    lines = data.readlines()
    data.close()

    data = open('data.txt', 'w')
    for line in lines:
        j=line.split()
        if(j[0]!=s):
            data.write(line)
    data.close()
def update(event):
    data=open('data.txt','r')
    s = s6.get()
    #s6.set("")

    lines = data.readlines()
    data.close()
    
    data=open('data.txt','w')

    for line in lines:

        j=line.split()

        if(j[0]==s):

            r1= s1.get()
            r2=s2.get()
            r3=s3.get()
            r4=s4.get()
            r5=s5.get()
            data.writelines(r1 + "  " + r2 + " " + r3 + " " + r4 + " " + " " + r5 + " " + '\n')
    updated()
    data.close()

def search(event):
    l3.grid(row=10,column=0)
    e6.grid(row=10,column=1)
    b5.bind('<Button-1>',ok)
    b7.bind('<Button-1>',delete)
    b8.bind('<Button-1>',update)

l1=Label(root,text='Energy Production Manager',fg='black',font=('Helvetica',30))
l2=Label(root,text='',fg='Black')


l3=Label(root,text='Resource Name',fg='black')
l4=Label(root,text='Resource Type',fg='black')
l5=Label(root,text='Production Cost For 1kj of energy',fg='black')
l6=Label(root,text='Estimated Remaining Amount',fg='black')
l7=Label(root,text='Contribution to Carbin Footprint',fg='black')
l8=Label(root,text='',fg='black')

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

e1=Entry(root,textvariable=s1)
e2=Entry(root,textvariable=s2)
e3=Entry(root,textvariable=s3)
e4=Entry(root,textvariable=s4)
e5=Entry(root,textvariable=s5)
e6=Entry(root,textvariable=s6)

l1.grid(row=0,columns=2)
l2.grid(row=1,column=0,sticky=W)

l3.grid(row=2,sticky=W)
l4.grid(row=3,sticky=W)
l5.grid(row=4,sticky=W)
l6.grid(row=5,sticky=W)
l7.grid(row=6,sticky=W)


e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)
e5.grid(row=6,column=1)

b1=Button(root,text='Next_Record',fg='Black')
b1.grid(row=8,column=1)

b2=Button(root,text='Add',fg='Black')
b2.grid(row=8,column=2)


b5=Button(root,text='Search',fg='Black')
b5.grid(row=8,column=3)

b7=Button(root,text='Delete',fg='Black')
b7.grid(row=8,column=4)

b8=Button(root,text='Update',fg='Black')
b8.grid(row=8,column=5)

b9=Button(root,text='Reset',fg='Black')
b9.grid(row=8,column=6)

#The Calling through Button    
b1.bind('<Button-1>',display)
b2.bind('<Button-1>',add)

b5.bind('<Button-1>',search)
b7.bind('<Button-1>',search)
b8.bind('<Button-1>',search)
b9.bind('<Button-1>',reset)

root.mainloop()

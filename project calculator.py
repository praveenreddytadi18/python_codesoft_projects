import tkinter
from tkinter import *
root=Tk()
root.title("calculator")
root.config(bg="black")
f=0
def bu(num):
    cu=display.get()
    cl()
    f=cu+num

    display.insert(0,f)
def cl():
    display.delete(0,END)
def de():
    display.delete(1,0)
def add():
    global a
    a="+"
    global g
    g=display.get()
    cl()
def sub():
    global a
    a="-"
    global g
    g=display.get()
    cl()
def mul():
    global a
    a="*"
    global g
    g=display.get()
    cl()
def div():
    global a
    a="/"
    global g
    g=display.get()
    cl()

def eq():
    global g
    f=display.get()
    cl()
    if a=="+":
        s=int(f)+int(g)
    elif a=="-":
        s=int(g)-int(f)
    elif a=="*":
        s=int(f)*int(g)
    elif a=="/":
        s=int(g)/int(f)
    else:
        s="error"
    display.insert(0,s)

display=Entry(root,width=25,font=('Timesnewroman',30),justify=RIGHT)
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
bu7=Button(root,text="7",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("7")).grid(row=2,column=0,padx=5,pady=2)
bu8=Button(root,text="8",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("8")).grid(row=2,column=1,padx=5,pady=2)
bu9=Button(root,text="9",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("9")).grid(row=2,column=2,padx=5,pady=2)
bu4=Button(root,text="4",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("4")).grid(row=3,column=0,padx=5,pady=2)
bu5=Button(root,text="5",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("5")).grid(row=3,column=1,padx=5,pady=2)
bu6=Button(root,text="6",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("6")).grid(row=3,column=2,padx=5,pady=2)
bu1=Button(root,text="1",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("1")).grid(row=4,column=0,padx=5,pady=2)
bu2=Button(root,text="2",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("2")).grid(row=4,column=1,padx=5,pady=2)
bu3=Button(root,text="3",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: bu("3")).grid(row=4,column=2,padx=5,pady=2)
bu0=Button(root,text="0",font=('Timesnewroman',20),padx=125,pady=20,command=lambda: bu("0")).grid(row=5,columnspan=2,column=0,padx=5,pady=2)
buc=Button(root,text="c",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: cl()).grid(row=1,column=0,padx=5,pady=2)


bue=Button(root,text="=",font=('Timesnewroman',20),padx=120,pady=20,command=lambda: eq()).grid(row=5,column=2,columnspan=2,padx=5,pady=2)
bua=Button(root,text="+",font=('Timesnewroman',20),padx=50,pady=120,command=lambda: add()).grid(row=2,rowspan=3,column=3,padx=5,pady=2)
bus=Button(root,text="-",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: sub()).grid(row=1,column=3,padx=5,pady=2)
bum=Button(root,text="*",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: mul()).grid(row=1,column=2,padx=5,pady=2)
bud=Button(root,text="/",font=('Timesnewroman',20),padx=50,pady=20,command=lambda: div()).grid(row=1,column=1,padx=5,pady=2)


root.mainloop()
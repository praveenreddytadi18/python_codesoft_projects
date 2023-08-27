import string
import random
from tkinter import *

root=Tk()
root.title("Password Generator")
root.geometry('600x400')

def generate():
    small_a=string.ascii_lowercase
    Capital_a=string.ascii_uppercase
    num=string.digits
    char=string.punctuation
    all = small_a +Capital_a+num+ char
    password_length=int(Length_box.get())
    pas= random.sample(all,password_length)

    if y.get()==1:
        Password_generator.delete(0, END)
        Password_generator.insert(0, random.sample(small_a+Capital_a,password_length))
    elif y.get()==2:
        Password_generator.delete(0, END)
        Password_generator.insert(0, random.sample(small_a + Capital_a+ num, password_length))
    elif y.get()==3:
        Password_generator.delete(0, END)
        Password_generator.insert(0, pas)

def cut():
    root.clipboard_append(Password_generator.get())


name=Label(root,text="Password generator",font=("Timesnewroman",20),justify='center')
name.grid(row=0)
p=Label(root,text="Level of Password",font=("Timesnewroman",20),justify='center')
p.grid(column=1)

y=IntVar()

easy_button=Radiobutton(root,text="Easy",font=("Timesnewroman",15),value=1,variable=y,justify='center',width=15).grid(row=2,column=1,pady=5)

medium_button=Radiobutton(root,text="Medium",font=("Timesnewroman",15),value=2,variable=y,justify='center',width=15).grid(row=3,column=1,pady=5)

strong_button=Radiobutton(root,text="Strong",font=("Timesnewroman",15),value=3,variable=y,justify='center',width=15).grid(row=4,column=1,pady=5)

password_length=Label(root,text="Length selector",font=("Timesnewroman",20),justify='center').grid(row=5,column=1)

Length_box=Spinbox(root,from_=4,to=50,width=15,font=("Timesnewroman",10),justify='center')
Length_box.grid(row=6,column=1)

Generate_button=Button(root,text="Generate",font=("Timesnewroman",15),justify='center',command=generate).grid(row=7,column=1,pady=5)

Password_generator=Entry(root,width=25)
Password_generator.grid(row=8,column=1)

Copy_button=Button(root,text="Copy",font=("Timesnewroman",15),justify='center',command=cut)
Copy_button.grid(row=9,column=1,pady=5)


root.mainloop()
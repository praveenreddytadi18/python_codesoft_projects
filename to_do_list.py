import tkinter.messagebox
from tkinter import *


root=Tk()
root.title("To do List")
root.geometry('600x400')

def adding():
    tod =task_add.get()
    if tod != "":
        todo_box.insert(END,tod)
        task_add.delete(0,END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION",message="Sorry you have not entered task")

def removing():
    try:
        inde=todo_box.curselection()[0]
        todo_box.delete(inde)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION", message="Sorry you have not selected task to be deleted")


frame=Frame(root)
frame.pack()

todo_box=Listbox(frame,height=20,width=50)
todo_box.pack(side=LEFT)

scroller=Scrollbar(frame)
scroller.pack(side=RIGHT,fill=Y)

todo_box.config(yscrollcommand=scroller.set)

task_add=Entry(root,font=9,width=50)
task_add.pack()

task_add_button=Button(root,text="Add task",font=6,bg="yellow",width=20,command=adding).pack()
task_remove_button=Button(root,text="Remove task",font=6,bg="yellow",width=20,command=removing).pack()


root.mainloop()
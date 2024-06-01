from tkinter  import *
from tkinter import messagebox

root=Tk()
root.geometry("600x550")
root.maxsize(width=600,height=550)
root.minsize(width=600,height=550)

def onmemberpage():
    top=Toplevel()
    top.geometry("600x550")
    top.maxsize(width=400,height=300)
    top.minsize(width=400,height=300)
    top.title("Member Page")
    top.configure(bg="light blue")
    top.resizable(width=False,height=False)
    username_label=Label(top,text="UserID",bg="light blue")
    username_label.grid(row=0,column=0)
    password_label=Label(top,text="Password",bg="light blue")
    password_label.grid(row=1,column=0)
    e1=Entry(top)
    e1.grid(row=0,column=1)
    e2=Entry(top)
    e2.grid(row=1,column=1)
    login_button=Button(top,text="Login",width=5,height=1,font="Roboto 10 bold",command=onmemberpage)
    login_button.grid(row=3,column=0)

    
def onadminpage():
    pass


b1=Button(root,text='Admin Login',width=10,height=2,font="Roboto 14 bold",command=onadminpage)
b1.place(relx=0.5, rely=0.4,anchor=CENTER)
b2=Button(root,text='Member Login',width=10,height=2,font="Roboto 14 bold",command=onmemberpage)
b2.place(relx=0.5, rely=0.5,anchor=CENTER)


root.mainloop()

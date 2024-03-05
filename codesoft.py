import random
from tkinter import *

root = Tk()
root.title("PASSWORD GENERATOR BY YOUSRA ")
root.geometry("450x400")

#Frames
frame = Frame(root, bg="black")
text = Label(frame, text="GENERATE YOUR PASSWARD", font=("Times New Roman", 12, "bold"), fg="white", bg="black", pady=10)
text.pack()
frame.pack(fill=X)


frame2 = Frame(root,bg="white")
text2 = Label(frame2,text="ENTER LENGTH : ",font=("Times New Roman",11,"bold"),fg="black",pady=10)
text2.pack(side=LEFT)
length = IntVar()
length_entered = Entry(frame2,textvariable=length,font=("Arial", 7,'bold'),width=80).pack(side=RIGHT)
frame2.pack()

frame3 = Frame(root, bg="white")
text3 = Label(frame3, text="ENTER AMOUNT : ", font=("Times New Roman", 11, "bold"), fg="black",pady=10)
text3.pack(side=LEFT)
amount = IntVar()
length_entered2 = Entry(frame3, textvariable=amount, font=("Arial", 7,'bold'),width=80).pack(side=RIGHT)
frame3.pack()


list = Listbox(root, justify=LEFT, width=40, height=15, font="Arial 8 bold")
list.place(y=150, x=110)


#Functions

def gen_password():
    global length
    global amount
    global password

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = uppercase.lower()
    digits = "0123456789"
    symbols = "`!@#$%^&*()-=[];',./~_+{}|:<>?"

    upper, lower, dig, syB = True, True, True, True
    all_values = ""
    if upper:
        all_values += uppercase
    if lower:
        all_values += lowercase
    if dig:
        all_values += digits
    if syB:
        all_values += symbols
    for i in range(amount.get()):
        password = "".join(random.sample(all_values,length.get()))
        list.insert(END,password)
    list.update()

def listbox_copy():
    root.clipboard_clear()
    selected = list.get(ANCHOR)
    root.clipboard_append(selected)

 #generate Button
global password
button = Button(root,text="GENERATE",font=("Arial",7,"bold"),command=gen_password,bg="gold").place(x=150,y=130,width=150,height=20)
#listbox
list = Listbox(root,justify=LEFT,width=40,height=15,font="Arial 8 bold")
list.place(y=150,x=110)
#copy button
button = Button(root,text="COPY",font=("Arial",7,"bold"),command=listbox_copy,bg="gold").place(x=150,y=375,width=150,height=20)

root.mainloop()
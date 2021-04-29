from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

def updatefunc():
    root = Tk()
    root.iconbitmap("student.ico")
    root.geometry('500x720+450+10')
    root.title("Update Student Details Form")
    root.resizable(FALSE,FALSE)
    Fullname=StringVar()
    Email=StringVar()
    Fathername=StringVar()
    Mothername=StringVar()
    Branchname=StringVar()
    Mobilenumber=StringVar()
    Gender=StringVar()
    ID=StringVar()
    checkbox=IntVar()
    
    def update_button1():
        def send_mail():
            EmailAdd = "govt.polytechnicdwarhatalmora@gmail.com" #senders Gmail id over here
            Pass = "9456350385A" #senders Gmail's Password over here
            msg = EmailMessage()
            msg['Subject'] = 'Congratulation You Are Alloted Seat in Spot Counsling'  # Subject of Email
            msg['From'] = EmailAdd
            msg['To'] =  Email.get() # Reciver of the Mail
            msg.set_content('You have been Alloted Seat in spot counslling.\n Your registerd details are as follows :-\n 'f'Your name is :{Fullname.get()}\n Your Email is :{Email.get()}\n Your Father name is :{Fathername.get()}\n Your Mother name is : {Mothername.get()}\n Your BranchName is :{Branchname.get()}\n Your name is :{Mobilenumber.get()}\n Your Gender is : {Gender.get()}\n .CheckIn to college with all the Documents. If all above details are correct no need to response this email if any details are incorrect contact the Adminstraion Office.')  # Email body or 
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Added Gmails SMTP Server
                smtp.login(EmailAdd, Pass)  # This command Login SMTP Library using your GMAIL
                smtp.send_message(msg)  # This Sends the message
                print('send successfully')
                # messagebox.showinfo("User Registered","User is registerd to the College")
        if(checkbox.get()==1):
            bookid=int(ID.get())
            branch=Branchname.get()
            conn = sqlite3.connect(f'Registration_of_Student{session.get()}.db')
            cursor=conn.cursor()
            cursor.execute(f'UPDATE {branch} SET Fullname =? ,Email=?,Father_Name=?,Mother_name=?,Branch=?,mobile=?,Gender=? WHERE ID = ?;',(Fullname.get(),Email.get(),Fathername.get(),Mothername.get(),Branchname.get(),Mobilenumber.get(),Gender.get(),bookid))
            conn.commit()
            conn.close()
            send_mail()
            messagebox.showinfo('Notification',"The Student Detail has been updated")
            
                #after the data inserted into database entry field will be empty============#
            Roll_number_entry_8.delete(0,END)
            Fullname_entry_1.delete(0, END)
            Email_entry_2.delete(0, END)
            Fathername_entry_4.delete(0, END)
            Mothername_entry_5.delete(0, END)
            Mobilenumber_entry_7.delete(0, END)
        else:
            messagebox.showerror("Response","Read terms and condition")

    #===============update deatils form==============#
    update_form_label=Label(root,text="Update Student Details",width=20,font=("bold", 18)).pack(side='top',pady=35)
    #===========================label and name entry========================#
    Fullname_label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    Fullname_label_1.place(x=80,y=170)
    Fullname_entry_1 = Entry(root,textvar=Fullname,width=30)
    Fullname_entry_1.place(x=240,y=170)
    #===========================label and Email entry========================#
    Email_label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    Email_label_2.place(x=68,y=220)

    Email_entry_2 = Entry(root,textvar=Email,width=30)
    Email_entry_2.place(x=240,y=220)
    #=============================gender label and entry==============#
    Gender_label_3 = Label(root, text="Gender ",width=20,font=("bold", 10))
    Gender_label_3.place(x=70,y=480)

    # Gender_entry_4 = Entry(root,textvar=Gender,width=30)
    # Gender_entry_4.place(x=240,y=270)
    Gender= ttk.Combobox(root,width =25,textvariable =Gender ,values = ["Male",
                                "Female",
                                "Transgender"])
    Gender.place(x=240,y=480)

#===========================label and father_name entry========================#
    Fathername_label_4 = Label(root, text="Father Name",width=20,font=("bold", 10))
    Fathername_label_4.place(x=70,y=320)

    Fathername_entry_4 = Entry(root,textvar=Fathername,width=30)
    Fathername_entry_4.place(x=240,y=320)

    #===========================label and Mother Name entry========================#
    Mothername_label_5 = Label(root, text="Mother Name",width=20,font=("bold", 10))
    Mothername_label_5.place(x=70,y=370)

    Mothername_entry_5 = Entry(root,textvar=Mothername,width=30)
    Mothername_entry_5.place(x=240,y=370)
    #===========================label and name entry========================#
    Branchname_label_6 = Label(root, text="Branch ",width=20,font=("bold", 10))
    Branchname_label_6.place(x=70,y=420)
    Branchname= ttk.Combobox(root,width =25,textvariable =Branchname ,values = ["Information_Technology",
                                "MOM_and_SP",
                                "Diploma_CSE",
                                "Diploma_Civil",
                                "Diploma_Pharmacy",
                                "Electronic_Enginnering"])
    Branchname.place(x=240,y=420)
    #===========================label and Mobile number entry========================#

    Mobilenumber_label_7 = Label(root, text="Mobile number",width=20,font=("bold", 10))
    Mobilenumber_label_7.place(x=70,y=270)
    Mobilenumber_entry_7 = Entry(root,textvar=Mobilenumber,width=30)
    Mobilenumber_entry_7.place(x=240,y=270)

    #===========================label and Rollnumber entry========================#
    Roll_number_label_8 = Label(root, text="Roll number",width=20,font=("bold", 10))
    Roll_number_label_8 .place(x=80,y=120)
    Roll_number_entry_8 = Entry(root,textvar=ID,width=30)
    Roll_number_entry_8.place(x=240,y=120)
    #===================session====================#
    session=StringVar()
    session_label=Label(root,text='Select Session year',font=("bold", 12)).place(x=80,y=530)
    session= ttk.Combobox(root,width =25,textvariable =session ,values = ["2021-22",
                                "2022-23",
                                "2023-24",
                                "2024-25",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29",
                                "2029-2030"])
    session.place(x=240,y=530)
    #terms and condition apply========#
    check_button=Checkbutton(root,text="All Above Details are required",variable=checkbox)
    check_button.place(x=90,y=580)
    copy=Label(root,text='Developed By Gaurav And Team ©',font=('bold',10),fg='white',bg='#BB001B')
    copy.pack(side='bottom',fill=X)
    #===========================BUtton widget========================#
    Button(root, text='Submit',width=20,bg='#BB001B',fg='white',command=update_button1).place(x=180,y=630)

    root.mainloop()
# updatefunc()
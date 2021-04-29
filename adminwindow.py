from tkinter import*
#=====importing self created module which will show the registartion form=======#
import registrationform
#=====importing self created module which will help in deleting student record from data base======#
import deletestudent
#=============importing selfcreated update student record ==============#
import updatestudent
#to import jpg image
import allotment #it will import module 
#importing view database
import tables
from PIL import ImageTk #it will import Pillow librart
import smtplib
from email.message import EmailMessage
import sqlite3
import allotedstudentrecords
def student():
    admin_window=Tk()
    admin_window.iconbitmap("student.ico")
    bg=ImageTk.PhotoImage(file="./images/login.jpg")
    bg_image=Label(admin_window,image=bg)
    bg_image.place(x=0,y=0,relwidth=1,relheight=1)
    width = admin_window.winfo_screenwidth()
    height = admin_window.winfo_screenheight()
    admin_window.geometry(f'{width}x{height-100}+0+0')
    admin_window.resizable(FALSE,FALSE)
    admin_window.title("Student Registration system")
    admin_text=Label(text="Spot Counslling Registration And Allotment System",font=("bold",30)).pack(side='top',pady=40)
    # admin_text.place(x=450,y=40)
    #======================registration window-=====================#
    Register_button=Button(admin_window,text="Register Student",relief=GROOVE,width=15,height=5,font=("bold", 10),command=registrationform.register,bg='#BB001B',fg='white')
    Register_button.place(x=70,y=150)
    #-=====================student  record====================#
    Delete_student=Button(admin_window,text="Delete Student",relief=GROOVE,width=15,height=5,font=("bold", 10),command=deletestudent.delete_student,bg='#BB001B',fg='white')
    Delete_student.place(x=70,y=350)
    #============================view databasetable=========================#
    View_table_button=Button(admin_window,text="View Registerd \n\n Students Records",relief=GROOVE,width=15,height=5,font=("bold", 10),command=tables.viewdatabase,bg='#BB001B',fg='white')
    View_table_button.place(x=70,y=550)
    #=================================update student ==================#
    update_button=Button(admin_window,text="Update Student",relief=GROOVE,width=15,height=5,font=("bold", 10),command=updatestudent.updatefunc,bg='#BB001B',fg='white')
    update_button.place(x=1150,y=350)
    #===========================student selection table================#
    Student_selection_button=Button(admin_window,text="Seat Allotment",relief=GROOVE,width=15,height=5,font=("bold", 10),command=allotment.selection,bg='#BB001B',fg='white')
    Student_selection_button.place(x=1150,y=150)
    #========================view alloted student records======================#
    View_Alloted_button=Button(admin_window,text="View Alloted \n\n Students Records",relief=GROOVE,width=15,height=5,font=("bold", 10),command=allotedstudentrecords.viewdatabase,bg='#BB001B',fg='white')
    View_Alloted_button.place(x=1150,y=550)
    copy=Label(admin_window,text='Developed By Gaurav And Team ©',font=('bold',8),fg='white',bg='#01796F')
    copy.pack(side='bottom',fill='x')
    # admin_window.destroy()
    admin_window.mainloop()
# student()

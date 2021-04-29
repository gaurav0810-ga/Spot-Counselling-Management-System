from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
#--------------------writing fucntion for registering student-------------------#


#----------------------admin window delete command====================#
def delete_student():
    root=Tk()
    root.iconbitmap("student.ico")
    root.geometry("400x450+450+90")
    root.resizable(FALSE,FALSE)
    root.title("Delete student data")
    Branchname=StringVar()
      

    ID=IntVar()
    Email=StringVar()
    def delete():
        # bookid=int(ID.get())
        bookid=ID.get()
        email=Email.get()
        branch=Branchname.get()
        conn = sqlite3.connect(f'Registration_of_Student{session.get()}.db') 
        cursor=conn.cursor()
        cursor.execute(f'delete from {branch} where ID=? OR Email=?',(bookid,email))
        conn.commit()
        conn.close()
        messagebox.showinfo('Notification',"The Student Detail has deleted")
    l2=Label(root,text="Branch Name",font=("bold", 12)).place(x=40,y=40)
    Branchname= ttk.Combobox(root,width =25,textvariable =Branchname,values = ["Information_Technology",
                                "MOM_and_SP",
                                "Diploma_CSE",
                                "Diploma_Civil",
                                "Diploma_Pharmacy",
                                "Electronic_Enginnering"])
    Branchname.place(x=180,y=40)
    label_8 = Label(root, text="Roll number",width=20,font=("bold", 12))
    label_8.place(x=10,y=100)
    
    entry_8 = Entry(root,textvar=ID,width='28',bg='light gray')
    entry_8.place(x=180,y=100)  
    session=StringVar()
    session_label=Label(root,text='Select Session year',font=("bold", 12)).place(x=10,y=160)
    session= ttk.Combobox(root,width =25,textvariable =session,values = ["2021-22",
                                "2022-23",
                                "2023-24",
                                "2024-25",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29",
                                "2029-2030"])
    session.place(x=180,y=160)
    label_9 = Label(root, text="Email ID",width=20,font=("bold", 12))
    label_9.place(x=10,y=220)
    
    entry_9 = Entry(root,textvar=Email,width='28',bg='light gray')
    entry_9.place(x=180,y=220) 
    delete_button=Button(root,text="Delete Student",command=delete,bg="#BB001B",fg='white')
    delete_button.place(x=180,y=280)
    copy=Label(root,text='Developed By Gaurav And Team ©',font=('bold',10),fg='white',bg='#01796F')
    copy.pack(side='bottom',fill=X)
    root.mainloop()
# delete_student()
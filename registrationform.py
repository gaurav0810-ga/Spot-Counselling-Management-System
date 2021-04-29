from tkinter import*
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import smtplib
from email.message import EmailMessage
from tkinter import filedialog
def select():
    file=filedialog.askopenfilename()
    print(file)
    with open(f"{file}",'rb') as f:
        global data
        data=f.read()
def register():
    root = Tk()
    root.geometry('720x720')
    root.resizable(FALSE,FALSE)
    # adminwindow.student.admin_window.destroy()
    
    root.iconbitmap("student.ico")
    root.title("Registration Form")
    Fullname=StringVar()
    Email=StringVar()
    Fathername=StringVar()
    Mothername=StringVar()
    Branchname=StringVar()
    Mobilenumber=StringVar()
    Gender=StringVar()
    addhar=StringVar()
    Dateofbirth=StringVar()
    jeeprank=StringVar()
    def record():
        name=FullName_entry_1.get()
        email=Email_entry_2.get()
        father=Father_entry_4.get()
        mother=Mother_entry_5.get()
        branch=Branchname.get()
        mobile=Mobile_entry_7.get()
        gender=Gender.get()
        Dob=Dateofbirth_entry.get()
        addhar=addhar_entry.get()
        category=categorys.get()
        sub_category=sub_category_combo.get()
        rank=int(jeeprank_entry.get())
        #=============================importing email from database===================#
            #==================email sending function=================#
        email11='gkhati275@gmail.com'
        password11='college'
        conn=sqlite3.connect('Email.db')
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS email(Email TEXT,password TEXT)')

        
        rows=cursor.execute('SELECT * FROM email')
        if rows=='':
            print('you are good to save data')
            cursor.execute('INSERT INTO email (Email,password)VALUES(?,?)',(email11,password11))
        else:
            for row in rows:
                print(row[0])
                print(row[1])
        conn.commit()
        conn.close()
        pass
        def send_mail():
                # email=Email_entry_2.get()
            EmailAdd = "govt.polytechnicdwarhatalmora@gmail.com" #senders Gmail id over here
            Pass = "9456350385A" #senders Gmail's Password over here
            msg = EmailMessage()
            msg['Subject'] = 'Registration Details College'  # Subject of Email
            msg['From'] = EmailAdd
            msg['To'] =  email # Reciver of the Mail
            msg.set_content('You have been succesfully registerd to spot counslling.\n your registerd details are as follows :-\n 'f'Your name is :{name}\n Your Email is :{email}\n Your Father name is :{father}\n Your Mother name is : {mother}\n Your BranchName is :-{branch}\n Your Mobile number  is :{mobile}\n Your Gender is :-{gender}.\n Date of birth is :-{Dob}.\n Your Addhar Number is :-{addhar}.\n\n Your Jeep Rank is{rank}.\n\nIf all above details are correct no need to response this email if any details are incorrect contact the Adminstraion Office.If you were alloted seat you will get a mail')  # Email body or Content
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EmailAdd, Pass)  # This command Login SMTP Library using your GMAIL
                smtp.send_message(msg)  # This Sends the message
                print('send successfully')
                messagebox.showinfo("User Registered","User is registerd to the College")
                FullName_entry_1.delete(0, END)
                Email_entry_2.delete(0, END)
                Father_entry_4.delete(0, END)
                Mother_entry_5.delete(0, END)
                Dateofbirth_entry.delete(0,END)
                addhar_entry.delete(0,END)
                jeeprank_entry.delete(0,END)
                Mobile_entry_7.delete(0, END)
        conn = sqlite3.connect(f'Registration_of_Student{session.get()}.db')
        cursor=conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {branch}( ID INTEGER PRIMARY KEY  AUTOINCREMENT,Fullname TEXT,Email TEXT,Father_Name TEXT,Mother_name TEXT,Branch Text,Mobile TEXT,Gender Text, Date_of_Birth TEXT,Addhar_number TEXT,Jeep_Rank INTEGER, Category TEXT ,Sub_category,Image BLOB)')
        cursor.execute(f'INSERT INTO {branch} (FullName,Email,Father_Name,Mother_name,Branch,mobile,Gender,Date_of_Birth,Addhar_number,Jeep_Rank,Category,Sub_category,Image) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,email,father,mother,branch,mobile,gender,Dob,addhar,rank,category,sub_category,data))
        conn.commit()
        conn.close()
        messagebox.showinfo("Information","You are registered to the Database")
        send_mail()


#==============================top label=========================#
             
    label_0= Label(root, text="Registration Form  For Spot  Counslling",font=("bold", 20))
    label_0.place(x=150,y=45)
#===================label and entry widget================#

    FullName_label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    FullName_label_1.place(x=80,y=130)
    FullName_entry_1 = Entry(root,textvar=Fullname,width =30)
    FullName_entry_1.place(x=240,y=130)

#===============================Email label and entry=================#
    Email_label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    Email_label_2.place(x=68,y=180)

    Email_entry_2 = Entry(root,textvar=Email,width =30)
    Email_entry_2.place(x=240,y=180)
#g============================gender level==================
    Gender_label_3 = Label(root, text="Gender ",width=20,font=("bold", 10))
    Gender_label_3.place(x=70,y=430)

    Gender= ttk.Combobox(root,width =25,textvariable =Gender ,values = ["Male",
                                "Female",
                                "Transgender"])
    Gender.place(x=240,y=430)
#===================father name netry and label==================#
    Father_label_4 = Label(root, text="Father Name",width=20,font=("bold", 10))
    Father_label_4.place(x=70,y=280)

    Father_entry_4 = Entry(root,textvar=Fathername,width =30)
    Father_entry_4.place(x=240,y=280)
#======================mother name entry==============#
    Mother_label_5 = Label(root, text="Mother Name",width=20,font=("bold", 10))
    Mother_label_5.place(x=70,y=330)

    Mother_entry_5 = Entry(root,textvar=Mothername,width =30)
    Mother_entry_5.place(x=240,y=330)
#========================branch label ===========and entry================#
    Branch_label_6 = Label(root, text="Branch ",width=20,font=("bold", 10))
    Branch_label_6.place(x=70,y=380)
    Branchname= ttk.Combobox(root,width =25,textvariable =Branchname ,values = ["Information_Technology",
                                "MOM_and_SP",
                                "Diploma_CSE",
                                "Diploma_Civil",
                                "Diploma_Pharmacy",
                                "Electronic_Enginnering"])
    Branchname.place(x=240,y=380)
    #-------------------------------date of birth------------------------------#
    Dateofbirth_label= Label(root, text="Date of birth DD/MM/YYYY ",width=20,font=("bold", 10))
    Dateofbirth_label.place(x=70,y=480)
    Dateofbirth_entry= Entry(root,textvar=Dateofbirth,width =30)
    Dateofbirth_entry.place(x=240,y=480)
    addhar_label=Label(root,text="Addhar card Number",width=20,font=("bold",10))
    addhar_label.place(x=70,y=530)
    addhar_entry=Entry(root,textvar=addhar,width =30)
    addhar_entry.place(x=240,y=530)
    jeeprank_label=Label(root,text="Student Jeep Rank")
    jeeprank_label.place(x=70,y=580)
    jeeprank_entry=Entry(root,textvar=jeeprank,width=30)
    jeeprank_entry.place(x=240,y=580)
#=====================mobile number entry and label==========#
    Mobile_label_7 = Label(root, text="Mobile number",width=20,font=("bold", 10))
    Mobile_label_7.place(x=70,y=230)

    Mobile_entry_7 = Entry(root,textvar=Mobilenumber,width =30)
    Mobile_entry_7.place(x=240,y=230)
    #====================================session lebal and drop down====================
    session=StringVar()
    session_label=Label(root,text='Select Session year').place(x=500,y=120)
    session= ttk.Combobox(root,width =25,textvariable =session ,values = ["2021-22",
                                "2022-23",
                                "2023-24",
                                "2024-25",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29",
                                "2029-2030"])
    session.place(x=500,y=150)
    #=================main combobox Value ======================#
    category=['General','Sc','ST','OBCs','TWF','EWS']
    #=====================sub_combobox==========================#
    sub_category_general=['Unreserved','Unreserved physical handicaped','opening freedom fighter','opening armed forces','opening girls']
    sub_category_Sc=['SC Unreserved','SC Unreserved physical handicaped','SC opening freedom fighter','SC opening armed forces','Sc opening girls']
    sub_category_ST=['ST Unreserved','ST Unreserved physical handicaped','ST opening freedom fighter','ST opening armed forces','ST opening girls']
    sub_category_OBCs=['OBCs Unreserved','OBCs Unreserved physical handicaped','OBCs opening freedom fighter','OBCs opening armed forces','OBCs opening girls']
    sub_category_TWF=['Tuition Fee Waiver']
    sub_category_EWS=['Economically Weaker Section']
    #====================changing sub combobox=====================#
    def pick_category(e):
        if categorys.get()=='General':
            sub_category_combo.config(value=sub_category_general)
            sub_category_combo.current(0)
        elif categorys.get()=='Sc':
            sub_category_combo.config(value=sub_category_Sc)
            sub_category_combo.current(0)
        elif categorys.get()=='ST':
            sub_category_combo.config(value=sub_category_ST)
            sub_category_combo.current(0)
        elif categorys.get()=='OBCs':
            sub_category_combo.config(value=sub_category_OBCs)
            sub_category_combo.current(0)
        elif categorys.get()=='TWF':
            sub_category_combo.config(value=sub_category_TWF)
            sub_category_combo.current(0)
        elif categorys.get()=='EWS':
            sub_category_combo.config(value=sub_category_EWS)
            sub_category_combo.current(0)
            #=====================================category drop down==============
    category_label=Label(root,text='Category',font=("bold", 10)).place(x=500,y=190)
    categorys=ttk.Combobox(root,value=category,width=30)
    categorys.current(0)
    categorys.place(x=500,y=220)
    categorys.bind('<<ComboboxSelected>>',pick_category)
    sub_category_label=Label(root,text='Sub Category',font=("bold", 10)).place(x=500,y=260)
    sub_category_combo=ttk.Combobox(root,value=[" "],width=30)

    sub_category_combo.place(x=500,y=290)
    image_label=Label(root,text="Student image",font=("bold", 10))
    image_label.place(x=500,y=330)
    image_butoon=Button(root,text="Choose Photo ",bg='dark gray',font=("bold", 10),command=select,width=14)
    image_butoon.place(x=500,y=360)
    Button(root, text='Submit',width=30,bg='#bb001b',fg='white',command=record).place(x=240,y=650)
    # drop_down=ttk.Combobox(root,width=25,textvariable=category,values=[])
    copy=Label(root,text='Developed By Gaurav And Team ©',font=('bold',8),fg='white',bg='#01796F')
    copy.pack(side='bottom',fill=X)
    root.mainloop()

# register()
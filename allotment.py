import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.message import EmailMessage
def selection():
    root=Tk()
    root.iconbitmap("student.ico")
    root.geometry('500x600')
    root.title("Seat Allotment")
    root.resizable(FALSE,FALSE)
    student=StringVar()
    Branchname=StringVar()            
            
    def select():
            def send_mail():
                EmailAdd = "govt.polytechnicdwarhatalmora@gmail.com" #senders Gmail id over here
                Pass = "9456350385A" #senders Gmail's Password over here
                msg = EmailMessage()
                msg['Subject'] = 'Registration Details College'  # Subject of Email
                msg['From'] = EmailAdd
                msg['To'] =  email # Reciver of the Mail
                msg.set_content('You have been Alloted Seat in spot counslling.\n your registerd details are as follows :-\n 'f'Your name is :{name}\n Your Email is :{email}\n Your Father name is :{father}\n Your Mother name is : {mother}\n Your BranchName is :{branch}\n Your name is :{mobile}\n Your Gender is : {gender}.\nYour Date Of birth {Dob}\n.Your Addhar Card number is{addhar}.\n Your Jeep Rank is {rank} If all above details are correct. Please Submit your all required document to college within 5-6 days') 
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Added Gmails SMTP Server
                        smtp.login(EmailAdd, Pass)  # This command Login SMTP Library using your GMAIL
                        smtp.send_message(msg)  # This Sends the message
                        print('send successfully')
                        messagebox.showinfo('email',f'Email send to selected students {name}')
            conn = sqlite3.connect(f'Registration_of_Student{session.get()}.db')
            rq=int(no_entry.get())
            category=categorys.get()
            print(category)
            branch=Branchname.get()
            print(branch)
            sub_category=sub_category_combo.get()
            print(sub_category)
            #AND Sub_category in({sub_category}) ,
            # SELECT * FROM Information_Technology WHERE Category IN("General") AND Sub_category IN("Unreserved");
            row=f'SELECT * FROM  {branch} WHERE Category IN ("{category}") AND Sub_category IN ("{sub_category}") ORDER BY Jeep_Rank ASC LIMIT {rq}'
            print(row)
            data=conn.execute(row)
            for row in data:
                name=row[1]
                email=row[2]
                father=row[3]
                mother=row[4]
                branch=row[5]
                mobile=row[6]
                gender=row[7]
                Dob=row[8]
                addhar=row[9]
                rank=row[10]
                conn = sqlite3.connect(f'Allotmentseats_of_students{session.get()}.db')
                cursor=conn.cursor()
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {branch} ( ID INTEGER PRIMARY KEY  AUTOINCREMENT,Fullname TEXT,Email TEXT,Father_Name TEXT,Mother_name TEXT,Branch Text,Mobile TEXT,Gender Text, Date_of_Birth TEXT,Addhar_number TEXT,Jeep_Rank INTEGER NOT NULL UNIQUE, categorys TEXT ,Sub_category )')
                cursor.execute(f'INSERT INTO {branch} (FullName,Email,Father_Name,Mother_name,Branch,mobile,Gender,Date_of_Birth,Addhar_number,Jeep_Rank,categorys ,Sub_category ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(name,email,father,mother,branch,mobile,gender,Dob,addhar,rank,category,sub_category))
                messagebox.showinfo('student selected',f'{name} is Selected \n\nFather name is {father}\n\n  Jeep Rank {rank}')
                conn.commit()
                conn.close()
                send_mail()
         
    title=Label(root,text='Seat Allotment',font=('bold',20))
    title.place(x=170,y=10)

    no=Label(root,text="Number of students\n to Allot Seat ",font=('bold',12))
    no.place(x=70,y=80)

    no_entry=Entry(root,textvar=student,width=30)
    no_entry.place(x=240,y=80)
    session=StringVar()
    session_label=Label(root,text='Select Session year',font=("bold", 12)).place(x=70,y=150)
    session= ttk.Combobox(root,width =25,textvariable =session ,values = ["2021-22",
                                "2022-23",
                                "2023-24",
                                "2024-25",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29",
                                "2029-2030"])
    session.place(x=240,y=150)
    Branch_label_6 = Label(root, text="Branch ",width=20,font=("bold", 12))
    Branch_label_6.place(x=70,y=220)
    Branchname= ttk.Combobox(root,width =25,textvar=Branchname ,values = ["Information_Technology",
                                "MOM_and_SP",
                                "Diploma_CSE",
                                "Diploma_Civil",
                                "Diploma_Pharmacy",
                                "Electronic_Enginnering"])

    Branchname.place(x=240,y=220)
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
    category_label=Label(root,text='Category',font=("bold", 12)).place(x=70,y=290)
    categorys=ttk.Combobox(root,value=category,width=30)
    categorys.current(0)
    categorys.place(x=240,y=290)
    categorys.bind('<<ComboboxSelected>>',pick_category)
    sub_category_label=Label(root,text='Sub Category',font=("bold", 12)).place(x=70,y=360)
    sub_category_combo=ttk.Combobox(root,value=[" "],width=30)

    sub_category_combo.place(x=240,y=360)
    button=Button(root,text="Select Student",width=14,height=4,command=select,bg='#BB001B',fg='white')
    button.place(x=200,y=430)
    copy=Label(root,text='Developed By Gaurav And Team ©',font=('bold',10),fg='white',bg='#00A86B')
    copy.pack(side='bottom',fill=X)
    root.mainloop()
# selection()

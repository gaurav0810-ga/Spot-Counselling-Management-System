from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def viewdatabase():
    root = Tk()
    root.iconbitmap("student.ico")
    root.title('Alloted Student Record View')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width-50}x{height-50}+0+0')
    root.resizable(FALSE,FALSE)
    frame1 = Frame(root, width=1000, height=700)
    frame1.pack()
    Branchname=StringVar()
    scroll_x=Scrollbar(frame1,orient=HORIZONTAL)
    scroll_y=Scrollbar(frame1,orient=VERTICAL)
    tree = ttk.Treeview(frame1, height=30,column=("ID", "Full NAME", "Email", "Father Name",
                                       "Mother Name", "Branch", "Mobile", "Gender", "Date of Birth", "Addhar Number", "Jeep Rank","Category","sub category","Student Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    tree['show']='headings'
    scroll_x.pack(side="bottom",fill='x')
    scroll_y.pack(side='right',fill='y')
#======================edit==========================#
    tree.column("ID",width=40,anchor=CENTER)
    tree.column("Full NAME",width=170,anchor=CENTER)
    tree.column("Email",width=170,anchor=CENTER)
    tree.column("Father Name",width=160,anchor=CENTER)
    tree.column("Mother Name",width=160,anchor=CENTER)
    tree.column("Branch",width=120,anchor=CENTER)
    tree.column("Mobile",width=100,anchor=CENTER)
    tree.column("Gender",width=90,anchor=CENTER)
    tree.column("Date of Birth",width=90,anchor=CENTER)
    tree.column("Addhar Number",width=170,anchor=CENTER)
    tree.column("Jeep Rank",width=160,anchor=CENTER)
    tree.column("Category",width=180,anchor=CENTER)
    tree.column("sub category",width=180,anchor=CENTER)
    tree.column("Student Photo",width=160,anchor=CENTER)
#===================================#

    tree.heading("ID", text="ID")
    tree.heading("Full NAME", text="Full NAME")
    tree.heading("Email", text="Email")
    tree.heading("Father Name", text="Father Name")
    tree.heading("Mother Name", text="Mother Name")
    tree.heading("Branch", text="Branch")
    tree.heading("Mobile", text="Mobile")
    tree.heading("Gender", text="Gender")
    tree.heading("Date of Birth", text="Date of Birth")
    tree.heading("Addhar Number", text="Addhar Number")
    tree.heading("Jeep Rank", text="Jeep Rank")
    tree.heading("Category",text="category")
    tree.heading("sub category",text="sub category")
    tree.heading("Student Photo", text="Student Photo")
    tree.pack()
    scroll_y.config(command=tree.yview)
    scroll_x.config(command=tree.xview)
    session=StringVar()
    session_label=Label(root,text='Select Session year',font=("bold", 12)).pack(side='left')
    session= ttk.Combobox(root,width =25,textvariable =session ,values = ["2021-22",
                                "2022-23",
                                "2023-24",
                                "2024-25",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29",
                                "2029-2030"])
    session.pack(side='left')
    Branch_label_6 = Label(root, text="Branch ",width=20,font=("bold", 12))
    Branch_label_6.pack(side='left')
    Branchname= ttk.Combobox(root,width =25,textvar=Branchname ,values = ["Information_Technology",
                                "MOM_and_SP",
                                "Diploma_CSE",
                                "Diploma_Civil",
                                "Diploma_Pharmacy",
                                "Electronic_Enginnering"])
    Branchname.pack(side='left')

    
    def View():
        if(Branchname.get() !=''and session.get()!='' ):
            branch=Branchname.get()
            conn = sqlite3.connect(f'Allotmentseats_of_students{session.get()}.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {branch}")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", END, values=row)
                conn.close()
        else:
            messagebox.showerror('Selection error','Please select something')
    button1 = Button(root, text="Display data",bg='#BB001B',fg='white',width=15,height=2, command=View)
    button1.pack(pady=10)
    # copy=Label(root,text='Devloped By Gaurav And Team ©',font=('bold',10),fg='white',bg='#BB001B')
    # copy.pack(side='bottom',fill=X)
    root.mainloop()
# viewdatabase()
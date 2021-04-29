from tkinter import *
import sqlite3
from PIL import ImageTk #pip install pillow
#====================adminwindow module============#
import adminwindow
from tkinter import messagebox
def login_window():
        root=Tk()
        root.iconbitmap("student.ico")
        root.title("Login System")
        root.geometry("1080x600+160+20")
        root.resizable(False,False)
        # self.root.maxsize(640,426)
        #background

        bg=ImageTk.PhotoImage(file="./images/login1.jpg")
        bg_image=Label(root,image=bg)
        bg_image.place(y=100)
        #frame login
        
        Frame_login=Frame(root,borderwidth=5,relief="sunken")
        Frame_login.place(x=450,y=100,height=410,width=640)
        #======================================#
        uservalue = StringVar()
        passwordvalue = StringVar()
        #============label=====================#
        title=Label(Frame_login,text="Admin Login Here",fg="#BB001B",font=("Times New Roman",40,"bold"))
        title.pack()

        # description=Label(Frame_login,text="Admin login",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white")
        # description.place(x=50,y=80)

        admin=Label(Frame_login,text="UserID:-",fg="#050f06",font=("Goudy old style ",20,"bold"))
        admin.place(x=50,y=135)
        
        admin_entry=Entry(Frame_login,textvariable=uservalue,bg="lightgray",borderwidth=4,relief="sunken",font=("Goudy old style ",14))
        admin_entry.place(x=230,y=135,width=250,height=30)
        
        #========================passwprd===============#
        admin_password=Label(Frame_login,text="Password:-",fg="#050f06",font=("Goudy old style ",20,"bold"))
        admin_password.place(x=50,y=180)
        
        admin_password_entry=Entry(Frame_login,textvariable=passwordvalue,bg="lightgray",font=("Goudy old style ",13),borderwidth=5,relief="sunken",show='*')
        admin_password_entry.place(x=230,y=180,width=250,height=30)


            #===========================================================================================================
        def login_button():
            admin ="Gaurav"
            password ="Gaurav@123"
            if(uservalue.get() == admin and passwordvalue.get() == password ):
                messagebox.showinfo("welcome",f"welcome {uservalue.get()}")
                root.destroy()
                adminwindow.student()
                #========using of self created modules======#
                
                
            else:
                messagebox.showerror("Error","Invalid inputs")

        login_button=Button(Frame_login,text="Log In",font=("Goudy old style",15,"bold"),borderwidth=4,relief="raised",bg="#BB001B",fg='White',command=login_button)
        login_button.place(x=250,y=270,width=150,height=50)
        copy=Label(root,text='Developed By Gaurav And Team ©',font=('bold',10),fg='white',bg='#01796F')
        copy.pack(side='bottom',fill=X)
        root.mainloop()
        
login_window()

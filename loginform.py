from tkinter import *
import mysql.connector

from tkinter import messagebox
from studentscreenclass import *
from adminscreenclass import *
from facultyscreenclass import *
from parentscreenclass   import *

baseWindow=Tk()
LoginScreen=baseWindow
### Database Login Function ##
def loginFunction():
    try:
        print("Submitted")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="490812",
            database="studentsmanagementsystem",
        )
        print("Tested Connection")
        ### GET USER-NAME ##
        username = enteruser.get()
        ## Get PASSWORD ###
        password = enterpass.get()
        ## Construct SQL Command ##
        sql = "select passwd from user_table where username='%s'"%(username)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        passwdsql = ''  
        print("here ",myresult)          
        for r in myresult:
            ### PASSWORD RETURNED from DATABASE
            passwdsql = r[0]
        if enterpass.get() == passwdsql:
            sql = "select role from user_table where username='%s'" %(username)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for r in myresult:
                ## Extracted Role for the user
                role = r
            messagebox.showinfo("Authentication","Login Successful !!!!!")

            ## Based on Role open corresponding screen #
            if r[0] == 'Student':
                ## login screen withdrew
                LoginScreen.withdraw()
                ### Class Initiaion - Create one Object for Student Class #
                studentS = Studentscreen(baseWindow,username)
                studentS.SetImage()
            elif r[0] == 'Admin':
                LoginScreen.withdraw()
                adminS = admin(baseWindow) 
            elif r[0] == 'Teacher': 
                LoginScreen.withdraw()
                facultyS = FACULTY(baseWindow,username)
            elif r[0] == 'Parent': 
                LoginScreen.withdraw()
                parentS  = Parentscreen(baseWindow,username)
        else:
            messagebox.showinfo("Authentication Error", "Check username and password")
    except mysql.connector.Error as err:
        print("ERROR OCCURED - More Details : {}".format(err))
        messagebox.showinfo("Authentication Error", "Check username and password")


## Front END Coding ## 

LoginScreen.title("login system")
LoginScreen.geometry('1920x1080+0+0')
titleLogin=Label(LoginScreen,text="UNIVERSITY MANAGEMENT SYSTEM", compound=CENTER,\
font=('times new roman',55,'bold'),bg='steelblue',fg='turquoise',bd=30,relief=GROOVE) 

#titleLogin.grid(row=20,column=700)
#titleLogin.config(image=logo)
titleLogin.place(x=0,y=10,relwidth=1)
Login_Frame=Frame(LoginScreen,bg='paleturquoise1')
Login_Frame.place(x=150,y=200)
lbluser=Label(Login_Frame,text='USERNAME',compound=LEFT,bg='paleturquoise1',font=('times new roman',20,'bold'))\
.grid(row=5,column=2,pady=30,padx=20,sticky=NE)
lblpass=Label(Login_Frame,text='PASSWORD*',compound=LEFT,bg='paleturquoise1',font=('times new roman',20,'bold'))\
.grid(row=6,column=2,pady=30,padx=20,sticky=E)
enteruser=Entry(Login_Frame,bg='white',fg='black',font=('times new roman',30,'bold'))
enteruser.grid(row=5,column=3,padx=20,pady=30,sticky=E)
enterpass=Entry(Login_Frame,bg='white',fg='black',show="*",font=('times new roman',30,'bold'))
enterpass.grid(row=6,column=3,padx=20,pady=30,sticky=E)
## Command Login Function to be executed when clicked on LOGIN Button #
btlogin=Button(Login_Frame,text='LOGIN',command=loginFunction,bg='darkslategray3',fg='gray3',font=('times new roman',20,'bold'))
btlogin.grid(row=11,column=4)   
baseWindow.mainloop()
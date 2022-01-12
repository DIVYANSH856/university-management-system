from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


UserDetail = []
dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="490812",
            database="studentsmanagementsystem"
         )
'''
def loginFunction():
    try:
        mydb = dbConnect
        username = 'naruto'
        sql = "select * from user_table where username='%s'"%(username)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
    except mysql.connector.Error as err:
        print("ERROR OCCURED - More Details : {}".format(err))
        messagebox.showinfo("Authentication Error", "Check username and password")
'''

class Parentscreen:
    def __init__(self,master,user):
        self.userName=user
        self.Parentscreen=Toplevel(master)
        self.Parentscreen.title('PARENT SCREEN')
        self.Parentscreen.geometry('1920x1080+0+0')
        self.titlestudent=Label(self.Parentscreen,text='        PARENT SCREEN       ',font=('times new roman',60,'bold'),bg='steelblue',fg='turquoise',bd=20,relief=GROOVE)
        self.titlestudent.grid(column=1,row=0,padx=10,pady=10)               
        
        self.ParentTabs = ttk.Notebook(self.Parentscreen)
        self.ParentTabs.grid(column=1,row=1,padx=10,pady=10)
        
        self.ParentFrame1 = Frame(self.ParentTabs,bg='steelblue',width=1500,height=600)
        self.ParentFrame2 = Frame(self.ParentTabs,bg='steelblue',width=1500,height=600)
        self.ParentFrame3 = Frame(self.ParentTabs,bg='steelblue',width=1500,height=600)
        
        self.lblfirstname=Label(self.ParentFrame1,     text='FIRST NAME of Student   ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=0,column=0,pady=1,padx=2)
        self.lblfarthername=Label(self.ParentFrame1,   text='FATHER NAME  ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=1,column=0,pady=1,padx=2)
        self.lblmothername=Label(self.ParentFrame1,    text='MOTHER NAME  ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=2,column=0,pady=1,padx=2)
        self.lblFphonenumber=Label(self.ParentFrame1,   text='Father PHONE NUMBER ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=3,column=0,pady=1,padx=2)
        self.lblMphonenumber=Label(self.ParentFrame1,   text='Mother PHONE NUMBER ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=4,column=0,pady=1,padx=2)
        self.lbladdress=Label(self.ParentFrame1,   text='Address ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=5,column=0,pady=1,padx=2)
        self.lblusername=Label(self.ParentFrame1,   text='Username ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=6,column=0,pady=1,padx=2)
        
        self.ParentTabs.add(self.ParentFrame1,text='PROFILE')
        self.ParentTabs.add(self.ParentFrame2,text='MARKS')

        self.FrameAllMarks = Frame(self.ParentFrame2)
        self.FrameAllMarks.grid(row=0,column=0,pady=1,padx=2,sticky=W)

        self.FrameMarksReport = Frame(self.ParentFrame2,width=100,height=60)
        self.FrameMarksReport.grid(row=1,column=0,pady=1,padx=2,sticky=W)
        self.btlogin=Button(self.ParentFrame2,text='Graph it',command=self.graphit,bg='darkslategray3',fg='gray3',font=('times new roman',20,'bold')).grid(row=14,column=4)  

        self.updateColumns()
        self.GetMarks()
        
    def updateColumns(self):
        imageFile = ''
        try:
            mydb = dbConnect
            username = self.userName
            sql = "select * from parent_info where username='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print("My RESULT {}".format(myresult))
            for i in range(7):
                a = Label(self.ParentFrame1,text=myresult[0][i],font=('times new roman',20,'bold'))
                a.grid(row=i,column=1,pady=1,padx=2)
        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
            messagebox.showinfo("Authentication Error", "Check username and password")    
            
    def GetMarks(self):
        cols = ('FIRST_NAME', 'LAST_NAME','TERM','SUBJECT','TOTAL MARK',"MARKS OBTAINED","PERCENTAGE")
        listBox = ttk.Treeview(self.FrameAllMarks, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.column(col, minwidth=0, width=100, stretch=False)
            listBox.heading(col, text=col,anchor='center')    
            listBox.grid(row=1, column=0)

        cols1 = ("TERM", "TOTAL MARK","MARKS OBTAINED","PERCENTAGE")
        listBox1 = ttk.Treeview(self.FrameMarksReport, columns=cols1, show='headings')
        # set column headings
        for col1 in cols1:
            print(col1)
            listBox1.column(col1, minwidth=0, width=100, stretch=False)
            listBox1.heading(col1, text=col1,anchor='center')    
            listBox1.grid(row=2, column=0)
        try:
            mydb = dbConnect
            username1 = "Sarthak123"
            sql = "select FIRST_NAME,LAST_NAME,EXAM_TERM,SUBJECT,TOTAL_MARKS,MARKS_OBTAINED,(MARKS_OBTAINED/TOTAL_MARKS)*100 as PERCENTAGE from MARKS where username='%s'"%(username1)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
                listBox.insert("", 'end', values=row)

            sql="select EXAM_TERM,Sum(TOTAL_MARKS) as TotalMarks,sum(MARKS_OBTAINED) as TotalMarksObtained,(sum(MARKS_OBTAINED)/Sum(TOTAL_MARKS))*100 as PERC from MARKS where username='%s' group by EXAM_TERM;"%(username1)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for row in myresult:
                print(row)
                listBox1.insert("", 'end', values=row)


        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
    def graphit(self):
        mydb = dbConnect
        username1="sarthak123"
        sql = "select EXAM_TERM,SUBJECT,TOTAL_MARKS,MARKS_OBTAINED,(MARKS_OBTAINED/TOTAL_MARKS)*100 as PERCENTAGE from MARKS where username='%s'"%(username1)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        hy1=[1,2,3,4]
        ut1=[1,2,3,4]
        subh=['','','','']
        subu=['','','','']
        a=0
        b=0
        for row in myresult:
            print(row)
            if(row[0]=='HALF_YEARLY'):
                hy1[a]=row[4]
                subh[a]=row[1]
                a=a+1
            elif(row[0]=='UNIT TEST 1'):
                ut1[b]=row[4]
                subu[b]=row[1]
                b=b+1
        plt.subplot(1,3,1)
        plt.plot(subh,hy1,color='red')
        plt.xlabel("SUBJECT")
        plt.ylabel("PERCENTAGE OBTAINED")
        plt.title('HALF YEARLY')
        plt.subplot(1,2,2)
        plt.plot(subu,ut1,color='g')
        plt.xlabel("SUBJECT")
        plt.ylabel("PERCENTAGE OBTAINED")
        plt.title('UNIT TEST 1')
        plt.show()
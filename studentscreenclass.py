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

class Studentscreen:
    def __init__(self,master,user):
        self.userName=user
        self.studentscreen=Toplevel(master)
        self.studentscreen.title('STUDENT SCREEN')
        self.studentscreen.geometry('1920x1080+0+0')
        self.titlestudent=Label(self.studentscreen,text='        STUDENT SCREEN       ',font=('times new roman',60,'bold'),bg='steelblue',fg='turquoise',bd=20,relief=GROOVE)
        self.titlestudent.grid(column=1,row=0,padx=10,pady=10)               
        
        self.StudentTabs = ttk.Notebook(self.studentscreen)
        self.StudentTabs.grid(column=1,row=1,padx=10,pady=10)
        
        self.StudentFrame1 = Frame(self.StudentTabs,bg='steelblue',width=1500,height=600)
        self.StudentFrame3 = Frame(self.StudentTabs,bg='steelblue',width=1500,height=600)
        self.StudentFrame4 = Frame(self.StudentTabs,bg='steelblue',width=1500,height=600)
        self.StudentFrame5 = Frame(self.StudentTabs,bg='steelblue',width=1500,height=600)
        self.StudentFrame6 = Frame(self.StudentTabs,bg='steelblue',width=1500,height=600)
        
        self.lblfirstname=Label(self.StudentFrame1,     text='FIRST NAME   ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=0,column=0,pady=1,padx=2)
        self.lbllastname=Label(self.StudentFrame1,      text='LAST NAME    ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=1,column=0,pady=1,padx=2)
        self.lblcurrentclass=Label(self.StudentFrame1,  text='CURRENT CLASS ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=2,column=0,pady=1,padx=2)
        self.lbldateofbirth=Label(self.StudentFrame1,   text='DATE OF BIRTH',bg='steelblue',font=('times new roman',15,'bold')).grid(row=3,column=0,pady=1,padx=2)
        self.lbladmissionNUMB=Label(self.StudentFrame1, text='ADMISSION NO.',bg='steelblue',font=('times new roman',15,'bold')).grid(row=4,column=0,pady=1,padx=2)
        self.lblfarthername=Label(self.StudentFrame1,   text='FATHER NAME  ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=5,column=0,pady=1,padx=2)
        self.lblmothername=Label(self.StudentFrame1,    text='MOTHER NAME  ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=6,column=0,pady=1,padx=2)
        self.lblphonenumber=Label(self.StudentFrame1,   text='PHONE NUMBER ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=7,column=0,pady=1,padx=2)
        self.btlogin=Button(self.StudentFrame5,text='Graph it',command=self.graphit,bg='darkslategray3',fg='gray3',font=('times new roman',20,'bold')).grid(row=14,column=4)  
       
        self.StudentTabs.add(self.StudentFrame1,text='PROFILE')
        self.StudentTabs.add(self.StudentFrame3,text='DATESHEET')
        self.StudentTabs.add(self.StudentFrame4,text='TIME TABLE')
        self.StudentTabs.add(self.StudentFrame5,text='MARKS')

        self.FrameAllMarks = Frame(self.StudentFrame5)
        self.FrameAllMarks.grid(row=0,column=0,pady=1,padx=2,sticky=W)

        self.FrameMarksReport = Frame(self.StudentFrame5,width=100,height=60)
        self.FrameMarksReport.grid(row=1,column=0,pady=1,padx=2,sticky=W)
      
        self.updateColumns()
        self.SetImage()
        self.GetMarks()
    
    def updateColumns(self):
        imageFile = ''
        try:
            mydb = dbConnect
            username = self.userName
            sql = "select * from student_information where username='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print("My RESULT {}".format(myresult))
            for i in range(8):
                a = Label(self.StudentFrame1,text=myresult[0][i],font=('times new roman',20,'bold'))
                a.grid(row=i,column=1,pady=1,padx=2)
            imageFile = myresult[0][9]
        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
            messagebox.showinfo("Authentication Error", "Check username and password")    
    def graphit(self):
        mydb = dbConnect
        username = self.userName
        sql = "select EXAM_TERM,SUBJECT,TOTAL_MARKS,MARKS_OBTAINED,(MARKS_OBTAINED/TOTAL_MARKS)*100 as PERCENTAGE from MARKS where username='%s'"%(username)
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

    
    def SetImage(self):
        try:
            mydb = dbConnect
            username = self.userName
            sql = "select * from student_information where username='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            imageFile = myresult[0][9]
            sql = "select class.datesheet,class.timetable from class,student_information where username='%s' and student_information.current_class=class.class_name"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            dateSheetImage = myresult[0][0]
            timeSheetImage = myresult[0][1]
        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
            messagebox.showinfo("Authentication Error", "Check username and password")    
        print("IMAGE FILE {}".format(imageFile))       
        self.image = Image.open(imageFile)
        self.image = ImageTk.PhotoImage(self.image)
        self.StudentPic = Label(self.StudentFrame1, image=self.image )
        self.StudentPic.image = self.image
        self.StudentPic.grid(row=0,column=3,rowspan=8,columnspan=2)

        self.image = Image.open(dateSheetImage)
        self.image = ImageTk.PhotoImage(self.image)
        self.DateSheetPic = Label(self.StudentFrame3, image=self.image )
        self.DateSheetPic.image=self.image
        self.DateSheetPic.grid(row=0,column=0,rowspan=8,columnspan=2)

        self.image = Image.open(timeSheetImage)
        self.image = ImageTk.PhotoImage(self.image)
        self.TimeSheetPic = Label(self.StudentFrame4, image=self.image )
        self.TimeSheetPic.image = self.image
        self.TimeSheetPic.grid(row=0,column=0,rowspan=8,columnspan=2)

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
            username = self.userName
            sql = "select FIRST_NAME,LAST_NAME,EXAM_TERM,SUBJECT,TOTAL_MARKS,MARKS_OBTAINED,(MARKS_OBTAINED/TOTAL_MARKS)*100 as PERCENTAGE from MARKS where username='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
                listBox.insert("", 'end', values=row)

            sql="select EXAM_TERM,Sum(TOTAL_MARKS) as TotalMarks,sum(MARKS_OBTAINED) as TotalMarksObtained,(sum(MARKS_OBTAINED)/Sum(TOTAL_MARKS))*100 as PERC from MARKS where username='%s' group by EXAM_TERM;"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for row in myresult:
                print(row)
                listBox1.insert("", 'end', values=row)


        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))

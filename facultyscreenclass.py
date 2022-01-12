from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
import tkinter as tk

dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="490812",
            database="studentsmanagementsystem"
         )

class FACULTY:
    def __init__(self,master,user):
        self.userName = user
        print("Initialize facult clawss")
        self.facultyscreen=Toplevel(master)
        self.facultyscreen.title('FACULTY')
        self.facultyscreen.geometry("1920x1080+0+0")
        titlefaculty=Label(self.facultyscreen,text='        FACULTY SCREEN          ',font=('times new roman',60,'bold'),bg='steelblue',fg='turquoise',bd=20,relief=GROOVE)
        titlefaculty.grid(column=0,row=0,padx=10,pady=10)
        
        self.FacultyTabs = ttk.Notebook(self.facultyscreen)
        self.FacultyTabs.grid(column=0,row=1,padx=10,pady=10)
        
        self.FacultyFrame1 = Frame(self.FacultyTabs,bg='steelblue',width=1500,height=600)
        self.FacultyFrame2 = Frame(self.FacultyTabs,bg='steelblue',width=1500,height=600)
        self.FacultyFrame3 = Frame(self.FacultyTabs,bg='steelblue',width=1500,height=600)
        self.FacultyFrame4 = Frame(self.FacultyTabs,bg='steelblue',width=1500,height=600)
        self.FacultyFrame5 = Frame(self.FacultyTabs,bg='steelblue',width=1500,height=600)
        
        lblfacultyname=Label(self.FacultyFrame1,text='FACULTY NAME',bg='steelblue',font=('times new roman',15,'bold')).grid(row=0,column=0,pady=1,padx=1)
        lblsubject=Label(self.FacultyFrame1,    text='SUBJECT     ',bg='steelblue',font=('times new roman',15,'bold')).grid(row=1,column=0,pady=1,padx=1)
        lblpost=Label(self.FacultyFrame1,       text='FACULTY POST',bg='steelblue',font=('times new roman',15,'bold')).grid(row=2,column=0,pady=1,padx=1)
        lbldate_of_birth=Label(self.FacultyFrame1,text='DATE OF BIRTH',bg='steelblue',font=('times new roman',15,'bold')).grid(row=3,column=0,pady=1,padx=1)
        lblphonenumber=Label(self.FacultyFrame1,  text='Phone Number',bg='steelblue',font=('times new roman',15,'bold')).grid(row=4,column=0,pady=1,padx=1)
        lblusername=Label(self.FacultyFrame1,text='USERNAME',bg='steelblue',font=('times new roman',15,'bold')).grid(row=5,column=0,pady=1,padx=1)
        

        lblfirstname=Label(self.FacultyFrame4,text='STUDENT FIRSTNAME',font=('times new roman',15,'bold')).grid(row=2,column=0,pady=1,padx=1,stick=NE)
        lbllastname=Label(self.FacultyFrame4,text='STUDENT LASTNAME',font=('times new roman',15,'bold')).grid(row=3,column=0,pady=1,padx=1,sticky=NE)
        lblclass=Label(self.FacultyFrame4,text='CLASS OF STUDENT',font=('times new roman',15,'bold')).grid(row=4,column=0,pady=1,padx=1,sticky=NE)
        self.Entry_student_firstname=Entry(self.FacultyFrame4,bg='white',fg='black',font=('times new roman',15,'bold'))
        self.Entry_student_firstname.grid(row=2,column=1,padx=1,pady=1,sticky=W)
        self.Entry_student_lastname=Entry(self.FacultyFrame4,bg='white',fg='black',font=('times new roman',15,'bold'))
        self.Entry_student_lastname.grid(row=3,column=1,padx=1,pady=1,sticky=W)
        self.Entry_student_class=Entry(self.FacultyFrame4,bg='white',fg='black',font=('times new roman',15,'bold'))
        self.Entry_student_class.grid(row=4,column=1,padx=1,pady=1,sticky=W)

        cols = ('FIRST_NAME','PHONE_NUMBER')
        self.listBox = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox.column(col, minwidth=0, width=100, stretch=False)
            self.listBox.heading(col, text=col,anchor='center')    
            self.listBox.grid(row=7, column=0)

        cols = ('FIRST_NAME', 'LAST_NAME','TERM','SUBJECT','TOTAL MARK',"MARKS OBTAINED","PERCENTAGE")
        self.listBox1 = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox1.column(col, minwidth=0, width=100, stretch=True)
            self.listBox1.heading(col, text=col,anchor='center')    
            self.listBox1.grid(row=7, column=1)

        cols = ("PresentDays","AbsentDays")
        self.listBox2 = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox2.column(col, minwidth=0, width=100, stretch=True)
            self.listBox2.heading(col, text=col,anchor='center')    
            self.listBox2.grid(row=7, column=2)

    
        def GetPhoneNumber():
            imageFile = ''
            try:
                mydb = dbConnect
                stFirstName = self.Entry_student_firstname.get()
                stLastName = self.Entry_student_lastname.get()
                stClass = self.Entry_student_class.get()
                sql = "select FIRST_NAME,PHONE_NUMBER from student_information where FIRST_NAME='%s' and LAST_NAME='%s' and CURRENT_CLASS='%s'"%(stFirstName,stLastName,stClass)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                print("My RESULT {}".format(myresult))
                for row in myresult:
                    print(row)
                    self.listBox.insert("", 'end', values=row)
                # for i in range(6):
                #     a = Label(self.FacultyFrame1,text=myresult[0][i],font=('times new roman',20,'bold'))
                #     a.grid(row=i,column=1,pady=1,padx=2)

            except mysql.connector.Error as err:
                print("ERROR OCCURED - More Details : {}".format(err))

        def GetReport():
            imageFile = ''
            try:
                mydb = dbConnect
                stFirstName = self.Entry_student_firstname.get()
                stLastName = self.Entry_student_lastname.get()
                stClass = self.Entry_student_class.get()
                sql = "select FIRST_NAME,LAST_NAME,EXAM_TERM,SUBJECT,TOTAL_MARKS,MARKS_OBTAINED,(MARKS_OBTAINED/TOTAL_MARKS)*100 as PERCENTAGE from MARKS where FIRST_NAME='%s' and LAST_NAME='%s' and CURRENT_CLASS='%s'"%(stFirstName,stLastName,stClass)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for row in myresult:
                    print(row)
                    self.listBox1.insert("", 'end', values=row)
                sql = "select count(*) as DaysPresent,(select count(*) as DaysAbset from attendence where ABSENT_PRESEN_PorA='A' and FIRST_NAME='%s' and LAST_NAME='%s' and CLASS_NAME='%s') as DaysAbsent from attendence where ABSENT_PRESEN_PorA='P' and FIRST_NAME='%s' and LAST_NAME='%s' and CLASS_NAME='%s'"%(stFirstName,stLastName,stClass,stFirstName,stLastName,stClass)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for row in myresult:
                    print(row)
                    self.listBox2.insert("", 'end', values=row)

                
                # for i in range(6):
                #     a = Label(self.FacultyFrame1,text=myresult[0][i],font=('times new roman',20,'bold'))
                #     a.grid(row=i,column=1,pady=1,padx=2)

            except mysql.connector.Error as err:
                print("ERROR OCCURED - More Details : {}".format(err))

        def ClearData():
            self.listBox1.destroy()
            self.listBox2.destroy()
            self.listBox.destroy()
            
            cols = ('FIRST_NAME','PHONE_NUMBER')
            self.listBox = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
            # set column headings
            for col in cols:
                self.listBox.column(col, minwidth=0, width=100, stretch=False)
                self.listBox.heading(col, text=col,anchor='center')    
                self.listBox.grid(row=7, column=0)

            cols = ('FIRST_NAME', 'LAST_NAME','TERM','SUBJECT','TOTAL MARK',"MARKS OBTAINED","PERCENTAGE")
            self.listBox1 = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
            # set column headings
            for col in cols:
                self.listBox1.column(col, minwidth=0, width=100, stretch=True)
                self.listBox1.heading(col, text=col,anchor='center')    
                self.listBox1.grid(row=7, column=1)

            cols = ("PresentDays","AbsentDays")
            self.listBox2 = ttk.Treeview(self.FacultyFrame4, columns=cols, show='headings')
            # set column headings
            for col in cols:
                self.listBox2.column(col, minwidth=0, width=100, stretch=True)
                self.listBox2.heading(col, text=col,anchor='center')    
                self.listBox2.grid(row=7, column=2)



        self.Button_GET_ATTENDENCE=Button(self.FacultyFrame4,text='GET PHONE NUMBER',command=GetPhoneNumber,bg='white',fg='black',font=('times new roman',15,'bold')).grid(row=6,column=0,padx=1,pady=1,sticky=W)
        self.Button_GET_MARKS=Button(self.FacultyFrame4,text='Get Report',command=GetReport,bg='white',fg='black',font=('times new roman',15,'bold')).grid(row=6,column=1,padx=1,pady=1,sticky=W)
        self.Button_Clear=Button(self.FacultyFrame4,text='ClearData',command=ClearData,bg='white',fg='black',font=('times new roman',15,'bold')).grid(row=6,column=2,padx=1,pady=1,sticky=W)

        self.FacultyTabs.add(self.FacultyFrame1,text='PROFILE')
        self.FacultyTabs.add(self.FacultyFrame2,text='TIMETABLE')
        self.FacultyTabs.add(self.FacultyFrame3,text='DATESHEET')
        self.FacultyTabs.add(self.FacultyFrame4,text='Student Information')

        self.updateColumns()
        self.SetImage()
        
    def updateColumns(self):
        imageFile = ''
        try:
            mydb = dbConnect
            username = self.userName
            sql = "select * from faculty_info where USERNAME='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print("My RESULT {}".format(myresult))
            for i in range(6):
                a = Label(self.FacultyFrame1,text=myresult[0][i],font=('times new roman',20,'bold'))
                a.grid(row=i,column=1,pady=1,padx=2)
        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))

    def SetImage(self):
        try:
            mydb = dbConnect
            firstname = self.Entry_student_firstname
            username = self.userName
            sql = "select * from faculty_info where USERNAME='%s'"%(username)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            timeTableImage = myresult[0][7]
            imageFile = myresult[0][8]
            sql = "select datesheet from class where class_name='12-A'"
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            dateSheetImage = myresult[0][0]
        except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
            messagebox.showinfo("Authentication Error", "Check username and password")    
        print("IMAGE FILE {}".format(imageFile))       
        self.image = Image.open(imageFile)
        self.image = ImageTk.PhotoImage(self.image)
        self.FacultyPic = Label(self.FacultyFrame1, image=self.image )
        self.FacultyPic.image = self.image
        self.FacultyPic.grid(row=0,column=3,rowspan=8,columnspan=2)

        self.image = Image.open(dateSheetImage)
        self.image = ImageTk.PhotoImage(self.image)
        self.DateSheetPic = Label(self.FacultyFrame3, image=self.image )
        self.DateSheetPic.image = self.image
        self.DateSheetPic.grid(row=0,column=0,rowspan=8,columnspan=2)

        self.image = Image.open(timeTableImage)
        self.image = ImageTk.PhotoImage(self.image)
        self.TimeTablePic = Label(self.FacultyFrame2, image=self.image )
        self.TimeTablePic.image = self.image
        self.TimeTablePic.grid(row=0,column=0,rowspan=8,columnspan=2)


from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter as tk

UserDetail = []
dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="490812",
            database="studentsmanagementsystem"
         )

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


class admin:
   def __init__(self,master):
      self.adminscreen=Toplevel(master)
      self.adminscreen.title('ADMIN SCREEN')
      self.adminscreen.geometry('1600x700+0+0')
      self.titleadmin=Label(self.adminscreen,text='            ADMIN SCREEN             ',\
      font=('times new roman',70,'bold'),bg='steelblue',fg='turquoise',bd=20,relief=GROOVE) 
      self.titleadmin.grid(column=1,row=0,padx=20,pady=20)
      admintabs= ttk.Notebook(self.adminscreen)
      admintabs.grid(row=1,column=1,padx=10,pady=10)
      adminframe1=Frame(admintabs,bg='steelblue',width=1500,height=600)
      adminframe2=Frame(admintabs,bg='steelblue',width=1500,height=600)
      adminframe3=Frame(admintabs,bg='steelblue',width=1500,height=600)
      admintabs.add(adminframe1,text='ADD NEW STUDENT')
      admintabs.add(adminframe2,text='UPDATE USER')
      admintabs.add(adminframe3,text='ADD NEW TEACHER')

      def add_Student():
         dataGui = [self.entryStudentfirstname.get(),self.entryStudentlastname.get(),self.entryStudentcurrentclass.get(),self.entryStudentdateofbirth.get(),self.entryStudentadmissionNumb.get(),self.entryStudentfarthername.get(),self.entryStudentmothername.get(),self.entryStudentphonenumber.get(),self.entryStudentusername.get(),self.entryStudentImage.get()]
         print(dataGui)
         sql = "insert into student_information (FIRST_NAME, LAST_NAME, CURRENT_CLASS, DATE_OF_BIRTH, ADMISSION_NUMBER, FARTHER_FULLNAME,MOTHER_NAME,PHONE_NUMBER,username,Image)  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(dataGui[0]),dataGui[1],dataGui[2],dataGui[3],dataGui[4],dataGui[5],dataGui[6],dataGui[7],dataGui[8],dataGui[9])
         try:
            mydb = dbConnect
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            print(sql)
            dataGui = [self.entryStudentusername.get(),self.entryStudentpassword.get()]
            print(dataGui)
            sql = "insert into user_table (username,passwd,role)  values('%s','%s','%s')" % (str(dataGui[0]),dataGui[1],'Student')
            mycursor.execute(sql)
            mydb.commit()
         except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))

      def add_teacher():
         dataGui = [self.entryTeacherNAMEOFTEACHER.get(),self.entryTeacherSUBJECT.get(),self.entryTeacherPOST.get(),self.entryTeacherBIRTHDATE.get(),self.entryTeacher.get(),self.entryTeacherclassteacher.get(),self.entryTeacherusername.get(),self.entryTeacherusername.get(),self.entryTeacherTT.get(),self.entryTeacherImage.get()]
         print(dataGui)
         sql = "insert into faculty_info (NAME_OF_FACULTY,_SUBJECT_,_POST_of_faculty,BIRTH_DATE,PHONE_NUMBER,CLASS_TEACHER_OF,USERNAME,TIMETABLE,image)\
             values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(dataGui[0]),dataGui[1],dataGui[2],dataGui[3],dataGui[4],dataGui[5],dataGui[6],dataGui[7],dataGui[8])
         try:
            mydb = dbConnect
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            print(sql)
            dataGui = [self.entryTeacherusername.get(),self.entryTeacherpassword.get()]
            print(dataGui)
            sql = "insert into user_table (username,passwd,role)  values('%s','%s','%s')" % (str(dataGui[0]),dataGui[1],'Teacher')
            mycursor.execute(sql)
            mydb.commit()
         except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
      
      def Update_Tables():
         try:
            dataGui = [self.entryUpdatestable.get(),self.entryUpdatescolumn.get(),self.entryUpdates_what_to_update.get(),self.entryUpdates_where.get()]
            print(dataGui)
            sql = "update %s set %s = %s where %s" % (dataGui[0],dataGui[1],dataGui[2],dataGui[3])
            print(sql)
            mydb = dbConnect
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
         except mysql.connector.Error as err:
            print("ERROR OCCURED - More Details : {}".format(err))
      
      lblfirstname=Label(adminframe1,text='FIRST NAME',bg='steelblue',fg='black',anchor=NE,font=('times new roman',20,'bold')).grid(row=0,column=0,pady=1,padx=2,sticky=NE)
      lbllastname=Label(adminframe1,text='LAST NAME',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=1,column=0,pady=1,padx=2,sticky=NE)
      lblcurrentclass=Label(adminframe1,text='CURRENT CLASS',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=2,column=0,pady=1,padx=2,sticky=NE)
      lbldateofbirth=Label(adminframe1,text='DATE OF BIRTH',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=3,column=0,pady=1,padx=2,sticky=NE)
      lbladmissionNumb=Label(adminframe1,text='ADMISSION NO.',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=4,column=0,pady=1,padx=2,sticky=NE)
      lblfarthername=Label(adminframe1,text='FATHER NAME',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=5,column=0,pady=1,padx=2,sticky=NE)
      lblmothername=Label(adminframe1,text='MOTHER NAME',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=6,column=0,pady=1,padx=2,sticky=NE)
      lblphonename=Label(adminframe1,text='CONTACT NO.',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=7,column=0,pady=1,padx=2,sticky=NE)
      lblusername=Label(adminframe1,text='USERNAME',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=8,column=0,pady=1,padx=2,sticky=NE)
      lblpassword=Label(adminframe1,text='PASSWORD',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=9,column=0,pady=1,padx=2,sticky=NE)
      lblStudentImage=Label(adminframe1,text='Image',bg='steelblue',fg='black',compound=LEFT,font=('times new roman',20,'bold')).grid(row=10,column=0,pady=1,padx=2,sticky=NE)

      self.entryStudentfirstname=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentfirstname.grid(row=0,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentlastname=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentlastname.grid(row=1,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentcurrentclass=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentcurrentclass.grid(row=2,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentdateofbirth=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentdateofbirth.grid(row=3,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentadmissionNumb=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentadmissionNumb.grid(row=4,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentfarthername=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentfarthername.grid(row=5,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentmothername=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentmothername.grid(row=6,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentphonenumber=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentphonenumber.grid(row=7,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentusername=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentusername.grid(row=8,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentpassword=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentpassword.grid(row=9,column=2,padx=1,pady=2,sticky=E)
      self.entryStudentImage=Entry(adminframe1,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryStudentImage.grid(row=10,column=2,padx=1,pady=2,sticky=E)

      lbltabel=Label(adminframe2,text='ENTER TABLE',bg='steelblue',fg='black',compound=LEFT,anchor=NW,font=('times new roman',20,'bold')).grid(row=0,column=0,pady=1,padx=2)
      lblcolumn=Label(adminframe2,text='ENTER COLUMN',bg='steelblue',fg='black',compound=LEFT,anchor=NW,font=('times new roman',20,'bold')).grid(row=1,column=0,pady=1,padx=2)
      lblwhere=Label(adminframe2,text='ENTER WHERE',bg='steelblue',fg='black',compound=LEFT,anchor=NW,font=('times new roman',20,'bold')).grid(row=2,column=0,pady=1,padx=2)
      lblwhat_to_update=Label(adminframe2,text='ENTER WHAT TO UPDATE',bg='steelblue',fg='black',anchor=NW,compound=LEFT,font=('times new roman',20,'bold')).grid(row=3,column=0,pady=1,padx=2)

      self.entryUpdatestable=Entry(adminframe2,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryUpdatestable.grid(row=0,column=1,padx=1,pady=2)
      self.entryUpdatescolumn=Entry(adminframe2,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryUpdatescolumn.grid(row=1,column=1,padx=1,pady=2)
      self.entryUpdates_where=Entry(adminframe2,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryUpdates_where.grid(row=2,column=1,padx=1,pady=2)
      self.entryUpdates_what_to_update=Entry(adminframe2,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryUpdates_what_to_update.grid(row=3,column=1,padx=1,pady=2)

      lblNAMEOFTEACHER=Label(adminframe3,text='NAME OF TEACHER',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=0,column=0,pady=1,padx=2,sticky=NE)
      lblSUBJECT=Label(adminframe3,text='SUBJECT',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=1,column=0,pady=1,padx=2,sticky=NE)
      lblPOST=Label(adminframe3,text='POST OF TEACHER',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=2,column=0,pady=1,padx=2,sticky=NE)
      lblBIRTHDATE=Label(adminframe3,text='BIRTH_DATE',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=3,column=0,pady=1,padx=2,sticky=NE)
      lblphonenumber=Label(adminframe3,text='PHONE_NUMBER',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=4,column=0,pady=1,padx=2,sticky=NE)
      lblclassteacher=Label(adminframe3,text=' CLASS_TEACHER_OF',bg='steelblue',fg='black',anchor=N,font=('times new roman',20,'bold')).grid(row=5,column=0,pady=1,padx=2,sticky=NE)
      lblusername=Label(adminframe3,text='USERNAME',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=6,column=0,pady=1,padx=2,sticky=NE)
      lblpassword=Label(adminframe3,text='PASSWORD',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=7,column=0,pady=1,padx=2,sticky=NE)
      lblTeacherTimeTable=Label(adminframe3,text='Timetable',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=8,column=0,pady=1,padx=2,sticky=NE)
      lblTeacherImage=Label(adminframe3,text='Image',bg='steelblue',fg='black',anchor=NW,font=('times new roman',20,'bold')).grid(row=9,column=0,pady=1,padx=2,sticky=NE)

      self.entryTeacherNAMEOFTEACHER=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherNAMEOFTEACHER.grid(row=0,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherSUBJECT=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherSUBJECT.grid(row=1,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherPOST=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherPOST.grid(row=2,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherBIRTHDATE=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherBIRTHDATE.grid(row=3,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacher=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacher.grid(row=4,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherclassteacher=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherclassteacher.grid(row=5,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherusername=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherusername.grid(row=6,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherpassword=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherpassword.grid(row=7,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherTT=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherTT.grid(row=8,column=2,padx=1,pady=2,sticky=E)
      self.entryTeacherImage=Entry(adminframe3,bg='white',fg='black',font=('times new roman',20,'bold'))
      self.entryTeacherImage.grid(row=9,column=2,padx=1,pady=2,sticky=E)


      submitbutton=Button(adminframe1,text='SUBMIT',command=add_Student).grid(row=11,column=2)
      updatebutton=Button(adminframe2,text='UPDATE',command=Update_Tables).grid(row=5,column=2)
      submitbutton=Button(adminframe3,text='SUBMIT',command=add_teacher).grid(row=11,column=2)
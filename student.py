from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os,random
from datetime import datetime
from tkinter import filedialog
import pyttsx3
import csv
import glob


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system ")
        
        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #first img     
        img=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\face-recognition.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

        #second img
        img1=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500, height=130)

        #third img
        img2=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550, height=130)
        
        #bg img
        img3=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\Stanford.jp.jpeg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=-50,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1500,height=600)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=580)
        
        img_left=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimgleft=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimgleft)
        f_lbl.place(x=0,y=0,width=720, height=100)
        
        #cureent course
        cureent_course_frame=LabelFrame(left_frame,bd=2,bg="grey",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        cureent_course_frame.place(x=2,y=105,width=650,height=105)
        #department
        dep_label=Label(cureent_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2)
        
        dep_combo=ttk.Combobox(cureent_course_frame,textvariable=self.var_dep,state="readonly",font=("arial",12,"bold"),width=17)
        dep_combo['values']=("select department","computer science")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #course
        course_std=Label(cureent_course_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std=ttk.Combobox(cureent_course_frame,textvariable=self.var_course,state="readonly",font=("arial",12,"bold"),width=17)
        com_txtcourse_std['value']=("Select Course","AI","IT","DS","IOT","CS")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        # year
        currunt_year=Label(cureent_course_frame,font=("arial",12,"bold"),text="Year:",bg="white")
        currunt_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_currunt_year=ttk.Combobox(cureent_course_frame,textvariable=self.var_year,state="readonly",font=("arial",12,"bold"),width=17)
        com_txt_currunt_year['value']=("Select Year","1st","2nd","3rd","4th")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,sticky=W,padx=2)
        # semster
        label_Semester=Label(cureent_course_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        
        comSemester=ttk.Combobox(cureent_course_frame,textvariable=self.var_semester,state="readonly",font=("arial",12,"bold"),width=17)
        comSemester['value']=("Select Semester","Odd Semster","Even semester")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)
        
        
        
        # student_class_Information
        class_student_frame=LabelFrame(left_frame ,padx=10,pady=5,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="darkgreen",bg="grey",text="Student Class Information")
        class_student_frame.place(x=2,y=220,width=650,height=250)
        #student id
        studentID_label=Label(class_student_frame,font=("arial",12,"bold"),text="StudentID No:",bg="white")
        studentID_label.grid(row=0,column=0,sticky=W,padx=2,pady=7) 
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=22,font=("arial",11,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=7)
        #student name
        lbl_Name=Label( class_student_frame,font=("arial",12,"bold"),text="Student Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry( class_student_frame,textvariable=self.var_std_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #divison
        lbl_div=Label(class_student_frame,font=("arial",12,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(class_student_frame,textvariable=self.var_div,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        #roll no
        lbl_roll=Label(class_student_frame,font=("arial",12,"bold"),text="Roll No:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_roll=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=22,font=("arial",11,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=7)
        #Gender
        lbl_gender=Label(class_student_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(class_student_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)
        #D.O.B
        lbl_dob=Label(class_student_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)
        #Email
        lbl_email=Label(class_student_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(class_student_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)
        #Phone no.
        lbl_phone=Label(class_student_frame,font=("arial",12,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)
        #address
        lbl_adderss=Label(class_student_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_adderss.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_adderss=ttk.Entry(class_student_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_adderss.grid(row=4,column=1,padx=2,pady=7)
        #teacher
        lbl_teacher=Label(class_student_frame,font=("arial",12,"bold"),text="Teacher Name:",bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_teacher=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=22,font=("arial",11,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=7)
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, text="Take Photo Smaple", value="Yes", variable=self.var_radio1)
        radiobtn1.grid(row=5, column=0,pady=10)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame, text="No Photo Smaple", value="No", variable=self.var_radio1)
        radiobtn2.grid(row=5, column=1,pady=10)

        img30 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img30 = img30.resize((320,70), Image.Resampling.LANCZOS)
        self.photoImg50 = ImageTk.PhotoImage(img30)
        youimg=Label(class_student_frame,image=self.photoImg50,bd=2,relief=RIDGE)
        youimg.place(x=320,y=190,width=310,height=70)
        
        #button frame
        ButtonFrame1=Frame(left_frame,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=470,width=650,height=30)

        ButtonFrame2=Frame(left_frame,bd=3,relief=RIDGE)
        ButtonFrame2.place(x=0,y=500,width=650,height=30)
        
         # ButtonFrame
        btnAddData=Button(ButtonFrame1,text="UPDATE",command=self.update_data, font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1,padx=1)

        btnUpdate=Button(ButtonFrame1,text="DELETE",command=self.delete_data, font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=2,padx=1)

        btnDelete=Button(ButtonFrame1,text="RESET",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3,padx=1)

        btnPhoto=Button(ButtonFrame1,text="SAVE ",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnPhoto.grid(row=0,column=0,padx=1)
        
        take_Photo_btn=Button(ButtonFrame2,text="Take Photo Sample ",command=self.genrate_dataset,font=("arial",11,"bold"),width=35,bg="blue",fg="white")
        take_Photo_btn.grid(row=0,column=0)
        
        take_Photo_btn=Button(ButtonFrame2,text="Update Photo Sample ",font=("arial",11,"bold"),width=35,bg="blue",fg="white")
        take_Photo_btn.grid(row=0,column=2)
        

        

        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=675,y=10,width=660,height=580)  
        
        img_right=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimgright=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimgright)
        f_lbl.place(x=0,y=0,width=720, height=130)
        
        #search system
        search_frame=LabelFrame(right_frame ,padx=10,pady=5,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="black",bg="white",text="Search system")
        search_frame.place(x=2,y=135,width=650,height=70)
        
        lblSearch=Label(search_frame,font=("arial",11,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=2,sticky=W,padx=5)
        
        self.serch_var=StringVar()
        search_combo=ttk.Combobox(search_frame,width=12,textvariable=self.serch_var,font=("times new roman",11),state="readonly")
        search_combo['values']=("Select Option","Phone no.","Roll no.","Department")
        search_combo.grid(row=0,column=3,sticky=W,padx=5)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=ttk.Entry(search_frame,width=25,textvariable=self.serchTxt_var,font=("times new roman",10))
        txtSearch.grid(row=0,column=4,padx=5)

        btnExit=Button(search_frame,text="SEARCH",font=("arial",12,"bold"),width=10,bg="blue",fg="white")
        btnExit.grid(row=0,column=5,padx=5)

        btnExit=Button(search_frame,text="SHOW ALL",font=("arial",12,"bold"),width=10,bg="blue",fg="white")
        btnExit.grid(row=0,column=6,padx=5)
        
        
        #Tabel frame
        Table_frame=Frame(right_frame,bd=4,relief=RIDGE)
        Table_frame.place(x=5,y=210,width=650,height=300)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="department")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)
            
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #function dedclration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.va_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,value=i)
            conn.commit() 
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set (data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" or self.var_roll.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where studentid=%s",(
            
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.va_std_id.get()
                                                                                                                                                                                     ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","student details sucessfully update completed",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    # delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
    #reset
    def reset_data(self):
        
        self.var_dep.set ("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Divison"),
        self.var_roll.set(""),
        self.var_gender.set("Mail"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
    # genrate data set or Take Photo sample
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="" or self.var_roll.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where studentid=%s",(
            
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.va_std_id.get()==id+1
                                                                                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                
                #load predefine data on face frontals from opencv
                face_classified=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classified.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minimum neighbor =5
                    # if faces == ():
                    #     return None
                    for (x,y,h,w) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        
                cap=cv2.VideoCapture(0)
                self.img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        self.img_id +=1
                        face=cv2.resize(face_cropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(self.img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(self.img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(self.img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generatig datasets completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    
                            
                        
                
                                 
                        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system ")
        
         # =============================== Variables===========================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first img     
        img=Image.open(r"H:\ML Project\Attendence system ML\college_images\smart-attendance.jpg")
        img=img.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700, height=200)

        #second img
        img1=Image.open(r"H:\ML Project\Attendence system ML\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=700, height=200)
        
        #bg img
        img3=Image.open(r"H:\ML Project\Attendence system ML\college_images\Stanford.jp.jpeg")
        img3=img3.resize((1530,600),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530, height=600)
        
        title_lbl=Label(bg_img,text="ATTENDENCE MANGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=-50,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1500,height=600)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=580)
        
        img_left=Image.open(r"H:\ML Project\Attendence system ML\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimgleft=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimgleft)
        f_lbl.place(x=0,y=0,width=720, height=100)
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=675,y=10,width=660,height=580)
        #Left label frame
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=115,width=655,height=300)
        
        # labeland Entry
        #attendance id
        attendanceID_label=Label(left_inside_frame,font=("arial",12,"bold"),text="AttendanceID No:",bg="white")
        attendanceID_label.grid(row=0,column=0,sticky=W,padx=2,pady=7) 
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,font=("arial",11,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=2,pady=7)
        
        #roll no
        rollLabel=Label(left_inside_frame,font=("arial",12,"bold"),text="Roll No:",bg="white")
        rollLabel.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font=("arial",11,"bold"))
        atten_roll.grid(row=0,column=3,padx=2,pady=7)
        
        #name
        NameLabel=Label( left_inside_frame,font=("arial",12,"bold"),text="Name:",bg="white")
        NameLabel.grid(row=1,column=0,sticky=W,padx=1,pady=8)

        atten_name=ttk.Entry( left_inside_frame,width=22,font=("arial",11,"bold"))
        atten_name.grid(row=1,column=1,padx=1,pady=8)
        
        #department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font=("comicsansns" ,11, "bold"))
        depLabel.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=22,font=("comicsansns" ,11, "bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font=("comicsansns" ,11, "bold"))
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=22,font=("comicsansns" ,11, "bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        #Date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font=("comicsansns" ,11, "bold"))
        dateLabel.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=22,font=("comicsansns" ,11, "bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendance status
        attendenceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("comicsansns" ,11, "bold"))
        attendenceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font=("comicsansns" ,11, "bold"),state="readonly")
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        #button
        ButtonFrame1=Frame(left_inside_frame,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=170,width=630,height=38)

        btnAddData=Button(ButtonFrame1,text="Import csv",command=self.importCsv,font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame1,text="Export csv",font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame1,text="Update",font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(ButtonFrame1,text="Reset",font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnReset.grid(row=0,column=3,padx=1)
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=675,y=10,width=660,height=470)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=640,height=400)
        
        #scroll table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
         
        self.AttendenceReportTable.heading("id",text="Attendance ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendance",text="Attendance status")
        
        self.AttendenceReportTable["show"]="headings"
        
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendance",width=100)
        
        self.AttendenceReportTable.pack(fil=BOTH,expand=1)
        
         
    #fetch data   
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    def importCsv(self):
       global mydata 
       fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
       with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
       
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
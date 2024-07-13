from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
import os
from train import Train 
from face_recognition import Face_Recognition
from attendence import Attendence
class Face_Recognition_system:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        #first img     
        img=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\Stanford.jp.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

        #second img
        img1=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\face-recognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500, height=130)

        #third img
        img2=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\u.jpg")
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=-50,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=200)

        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=300,width=200,height=40)
        
        #Detect Face button
        img5=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\face_detector1.jpg")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=200,height=200)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=400,y=300,width=200,height=40)

        #Attendance button
        img6=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\report.jpg")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=100,width=200,height=200)

        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=700,y=300,width=200,height=40)

        #Help button
        img7=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=200,height=200)

        b1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1000,y=300,width=200,height=40)

        #Train button
        img8=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\Train.jpg")
        img8=img8.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=350,width=200,height=200)

        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=550,width=200,height=40)

        #photo button
        img9=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=350,width=200,height=200)

        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=400,y=550,width=200,height=40)

        #Developer button
        img10=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=700,y=350,width=200,height=200)

        b1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=700,y=550,width=200,height=40) 

        #Exit button
        img11=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\exit.jpg")
        img11=img11.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=350,width=200,height=200)

        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1000,y=550,width=200,height=40) 
    
    def open_img(self):
        os.startfile("data")
        
    #exit function
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Detector System","Confirm you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
        #function buttons
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
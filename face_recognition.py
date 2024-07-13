from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system ")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=-50,y=0,width=1530,height=45)
        
        #1st image
        img_top=Image.open(r"H:\ML Project\Attendence system ML\college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=45,width=650, height=690)
        
        #2nd image
        img_bottom=Image.open(r"H:\ML Project\Attendence system ML\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimgbottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimgbottom)
        f_lbl.place(x=650,y=45,width=950, height=690)
        
        #button
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.detect_face,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1.place(x=375,y=610,width=200,height=40)

    
    #attendence
    def mark_attendace(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split(",")
                name_List.append(entry[0])
            if ((i not in name_List) and (r not in name_List) and(n not in name_List)  and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        
    #face recognition
    def detect_face(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coords=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                # id,pred=clf.predict(gray_image[y:y+h,x:x+w])
                id,pred=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-pred/300)))
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="student",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where studentid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select roll from student where studentid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select dep from student where studentid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select studentid from student where studentid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                if confidence>77:
                    cv2.putText(img,f"studentid:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendace(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
                # self.mark_attendace(k,s,i) 
                coords=[x,y,w,h]    
            return coords

        def recognize(img,clf,faceCascade):
            coords=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        Video_Capture=cv2.VideoCapture(0)

        while True:
            ret,img=Video_Capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Detector",img)
            if cv2.waitKey(1)==13:
                break    
        Video_Capture.release()
        messagebox.showinfo("Attendance Report","Attendance Saved in csv file",parent=self.root)
        cv2.destroyAllWindows()
        
                    
                    
                    
            
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
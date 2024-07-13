from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system ")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=-50,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\face-recognition.png")
        img_top=img_top.resize((1400,325),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=45,width=1400, height=335)
        
        # Button
        b1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=0,y=375,width=1400,height=60)
        
        img_bottom=Image.open(r"C:\Users\Akshat Jain\Downloads\Attendence system ML (1)\Attendence system ML\college_images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1400,300),Image.Resampling.LANCZOS)
        self.photoimgbottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimgbottom)
        f_lbl.place(x=0,y=430,width=1400, height=300)
        
    def train_classifier(self):
        data_dir="data"
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L');  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #train the calssifier and save
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!",parent=self.root)
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
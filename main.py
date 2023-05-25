from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from Student import Student
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from attendence import Attendence
from help import Help
import os
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x650+0+0")
        self.root.title("Face_Recognition_System")
        # first image
        img = Image.open(r"D:\Face Recognition System\images\first.jpg")
        img = img.resize((370,100),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=370,height=100)
        # second image
        img1=Image.open(r"D:\Face Recognition System\images\top1.jpg")
        img1=img1.resize((260,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=370,y=0,width=260,height=100)
        # third image
       # img3=Image.open(r"D:\Face Recognition System\images\top3.jpg")
       # img3=img3.resize((220,100),Image.LANCZOS)
       #3 self.photoimg3=ImageTk.PhotoImage(img3)

       # f_lbl3=Label(self.root, image=self.photoimg3)
       # f_lbl3.place(x=600,y=0,width=200,height=100)
        # forth image
        img4=Image.open(r"D:\Face Recognition System\images\top4.jpg")
        img4=img4.resize((260,100),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl4=Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=630,y=0,width=260,height=100)
        # fifth image
        img5=Image.open(r"D:\Face Recognition System\images\top5.jpg")
        img5=img5.resize((380,100),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl5=Label(self.root, image=self.photoimg5)
        f_lbl5.place(x=890,y=0,width=380,height=100)
        # bg image
        img2=Image.open(r"D:\Face Recognition System\images\bg.jpg")
        img2=img2.resize((1400,550),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0,y=100,width=1400,height=550)

        title_lbl=Label(f_lbl2,text="Face Recognition Attendence System Software *****",font=("Times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        # student datails
        img6=Image.open(r"D:\Face Recognition System\images\studentdetails.jpg")
        img6=img6.resize((200,200),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_lbl2, image=self.photoimg6,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=50,width=200,height=200)

        b1_1=Button(f_lbl2,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=150,y=220,width=200,height=30)

        # face detector
        img7=Image.open(r"D:\Face Recognition System\images\top3.jpg")
        img7=img7.resize((200,200),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2=Button(f_lbl2, image=self.photoimg7,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=50,width=200,height=200)

        b2_1=Button(f_lbl2,text="Face Detection",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=400,y=220,width=200,height=30)

        # Attendence
        img8=Image.open(r"D:\Face Recognition System\images\images.jpg")
        img8=img8.resize((200,200),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b3=Button(f_lbl2, image=self.photoimg8,cursor="hand2",command=self.attendence_data)
        b3.place(x=650,y=50,width=200,height=200)

        b3_1=Button(f_lbl2,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b3_1.place(x=650,y=220,width=200,height=30)

        # Chatbot
        img9=Image.open(r"D:\Face Recognition System\images\chatbot.jpg")
        img9=img9.resize((200,200),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b4=Button(f_lbl2, image=self.photoimg9,cursor="hand2",command=self.help)
        b4.place(x=900,y=50,width=200,height=200)

        b4_1=Button(f_lbl2,text="Help Desk",command=self.help,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b4_1.place(x=900,y=220,width=200,height=30)
        #....
        # Train data
        img10=Image.open(r"D:\Face Recognition System\images\traindata.jpg")
        img10=img10.resize((200,200),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b5=Button(f_lbl2, image=self.photoimg10,command=self.train_data,cursor="hand2")
        b5.place(x=150,y=300,width=200,height=200)

        b5_1=Button(f_lbl2,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b5_1.place(x=150,y=470,width=200,height=30)

        # Photos
        img11=Image.open(r"D:\Face Recognition System\images\photo.jpg")
        img11=img11.resize((200,200),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b6=Button(f_lbl2, image=self.photoimg11,command=self.open_img,cursor="hand2")
        b6.place(x=400,y=300,width=200,height=200)

        b6_1=Button(f_lbl2,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b6_1.place(x=400,y=470,width=200,height=30)

        # Developer
        img12=Image.open(r"D:\Face Recognition System\images\developer.jpg")
        img12=img12.resize((200,200),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b7=Button(f_lbl2, image=self.photoimg12,cursor="hand2",command=self.developer)
        b7.place(x=650,y=300,width=200,height=200)

        b7_1=Button(f_lbl2,text="Developer",command=self.developer,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b7_1.place(x=650,y=470,width=200,height=30)

        # Exit
        img13=Image.open(r"D:\Face Recognition System\images\exit.jpg")
        img13=img13.resize((200,200),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b8=Button(f_lbl2, image=self.photoimg13,cursor="hand2",command=self.iExit)
        b8.place(x=900,y=300,width=200,height=200)

        b8_1=Button(f_lbl2,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b8_1.place(x=900,y=470,width=200,height=30)

        
    def open_img(self):
        os.startfile("data") 
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
    # buttons 
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
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



if __name__ == "__main__":
    root =Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    

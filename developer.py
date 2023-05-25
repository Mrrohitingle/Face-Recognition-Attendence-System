from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x650+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1350,height=50)

        img_top=Image.open(r"D:\Face Recognition System\images\d.jpg")
        img_top=img_top.resize((1350,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1350,height=600)
        
        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=500)

        img_top1=Image.open(r"D:\Face Recognition System\images\rohit.jpg")
        img_top1=img_top1.resize((150,125),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=290,y=0,width=150,height=125)

        # Developer Info
        dev_lable=Label(main_frame,text="Hello, We are from BS4_6 Group",font=("times new roman",13,"bold"),bg="white")
        dev_lable.place(x=0,y=5)

        img_top2=Image.open(r"D:\Face Recognition System\images\rohit.jpg")
        img_top2=img_top2.resize((150,125),Image.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=290,y=125,width=150,height=125)

        dev_lable1=Label(main_frame,text="1.Aniket Rahne(97)",font=("times new roman",13,"bold"),bg="white")
        dev_lable1.place(x=0,y=40)

        img_top3=Image.open(r"D:\Face Recognition System\images\rohit.jpg")
        img_top3=img_top3.resize((150,125),Image.LANCZOS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=290,y=250,width=150,height=125)

        dev_lable2=Label(main_frame,text="2.Achyut Sarangdhar(107)",font=("times new roman",13,"bold"),bg="white")
        dev_lable2.place(x=0,y=125)

        img_top4=Image.open(r"D:\Face Recognition System\images\rohit.jpg")
        img_top4=img_top4.resize((150,125),Image.LANCZOS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)

        f_lbl=Label(main_frame,image=self.photoimg_top4)
        f_lbl.place(x=290,y=375,width=150,height=125)

        dev_lable3=Label(main_frame,text="3.Vedant Gorde(124)",font=("times new roman",13,"bold"),bg="white")
        dev_lable3.place(x=0,y=250)

 
        dev_lable4=Label(main_frame,text="4.Rohit Ingle(135)",font=("times new roman",13,"bold"),bg="white")
        dev_lable4.place(x=0,y=375)



        





if __name__ == "__main__":
    root =Tk()
    obj =Developer(root)
    root.mainloop()

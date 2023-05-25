from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x650+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1350,height=50)

        img_top=Image.open(r"D:\Face Recognition System\images\he.jpg")
        img_top=img_top.resize((1350,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1350,height=600)

        dev_lable=Label(f_lbl,text="E-mail: sybbs406@mail.com",font=("times new roman",15,"bold"),bg="green")
        dev_lable.place(x=710,y=250)










if __name__ == "__main__":
    root =Tk()
    obj =Help(root)
    root.mainloop()

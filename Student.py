from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x650+0+0")
        self.root.title("Face_Recognition_System")

#Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
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
        img2=img2.resize((1270,550),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0,y=100,width=1270,height=550)

        title_lbl=Label(f_lbl2,text="Student Management System",font=("Times new roman",30,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1270,height=45)

        main_frame=Frame(f_lbl2,bd=2)
        main_frame.place(x=10,y=55,width=1270,height=490)
    #left label frame
        Left_frame=LabelFrame(main_frame,bd=2)
        Left_frame.place(x=10,y=10,width=730,height=490)
            
        #img_left=Image.open(r"D:\Face Recognition System\images\top3.jpg")
        #img_left=img_left.resize((720,130),Image.LANCZOS)
        #self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl3=Label( Left_frame,text="Student Details",font=("Times new roman",20,"bold"),bg="navy",fg="white")
        f_lbl3.place(x=0,y=0,width=725,height=35)

    #current course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=40,width=720,height=125)

    #Department
        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    #Course
        course_lable=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    #Year
        year_lable=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

    #Semester
        semester_lable=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_lable.grid(row=1,column=2,padx=10,sticky=W)

        Search_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        Search_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Search_combo.current(0)
        Search_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Right label frame
        # Right_frame=LableFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        #Right_frame.place(x=750,y=10,width=720,height=580)

    #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=165,width=720,height=350)

    #Student id
        studentId_lable=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #Student name
        studentName_lable=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #class division
        class_div_lable=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
    #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W )

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


    #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
            
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

    #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W )

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

    #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
            
    # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

    #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=715,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font =("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font =("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font =("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font =("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font =("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font =("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


    #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("times new roman",13,"bold"))
        Right_frame.place(x=740,y=10,width=520,height=580)

        img_right=Image.open(r"D:\Face Recognition System\images\top3.jpg")
        img_right=img_right.resize((520,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl3=Label(Right_frame, image=self.photoimg_right)
        f_lbl3.place(x=5,y=0,width=520,height=150)
            

    #==================Search System ===============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=700,height=70)

        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select ","Roll-No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        Search_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",width=12,font =("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(Search_frame,text="ShowAll",width=12,font =("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)


    #=====================Table Frame =================

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self .student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text ="Department ")
        self.student_table.heading("course",text ="Course ")
        self.student_table.heading("year",text ="Year ")
        self.student_table.heading("sem",text ="Semester ")
        self.student_table.heading("id",text ="Student ")
        self.student_table.heading("name",text="Name ")
        self.student_table.heading("roll",text ="Roll_No ")
        self.student_table.heading("gender",text="Gender ")
        self.student_table.heading("div",text ="Division ")
        self.student_table.heading("dob",text ="DOB ")
        self.student_table.heading("email",text ="Email ")
        self.student_table.heading("phone",text ="Phone ")
        self.student_table.heading("address",text ="Address ")
        self.student_table.heading("teacher",text ="Teacher ")
        self.student_table.heading("photo",text ="PhotoSampleStatus ")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
        #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sudosu",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
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
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

     #fetch data
    def fetch_data(self):
        conn= conn=mysql.connector.connect(host="localhost",username="root",password="sudosu",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
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
        
    #update
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sudosu",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
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
                    self.var_std_id.get()

                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully upadte completed",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
     
    #delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sudosu",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from Student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfully Deleted Student Details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)            
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

        #=======Generate data se or take photo Sample=======
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sudosu",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
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
                self.var_std_id.get()==id+1

                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===load predefineddata on face frontals from opencv====

                face_classifier=cv2.CascadeClassifier("D:\Face Recognition System\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.1,3,0)
                    #Scalling Factor
                    #Minimum Neighbour=5


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data sets Completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

                        

if __name__ == "__main__":
    root =Tk()
    obj = Student(root)
    root.mainloop()


  




















































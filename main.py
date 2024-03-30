from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter
import random 
import speech_recognition as spr
import re
from PIL import Image
import time as t
import smtplib
import pyttsx3
import mysql.connector
from pdf_mail import sendpdf
from fpdf import FPDF


class UserData:
    def __init__(self):
        self.treatment = []
        self.causes = []
        self.dieases = []  
        self.details = []
        self.personal = []
        self.result=""

class Login:
     
    def __init__(self,root):
      
        self.root=root
        self.root.geometry("1380x720+0+0")
        def fillname():
            text=text1.get(1.0,END)
            if(len(text) <= 0):return True
        def validate_email():
        
            if(fillname()) :
                messagebox.showwarning("Missing Statements","Please Provide All the Details")
                text2.delete(1.0,END)
                return 
            reg= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            text=text2.get(1.0,END)
            print(text)
            if not(re.match(reg,text)):
                messagebox.showerror("Invalid Email","Error: Your Email is Not Valid")
                text2.delete(1.0,END)
            else:
                messagebox.showinfo("Get OTP","Getting otp from your registered Email")
                Dt.personal.append(text1.get(1.0,END))
                Dt.personal.append(generateID())
                Dt.personal.append(text)
                send_email()

        def generate_otp():
            str="abcdefghijklmnipqrstuvwxyx0123456789"
            res="Hi , Your OTP is "
            for i in range(10):
                res+=str[random.randrange(0,len(str),1)]
            print(res)
            return res

        def verify_otp():
            global password
            if(len(password)!=27):
                messagebox.showwarning("Missing Statements","Please Provide All the Details")
                text3.delete(1.0,END)
                return 
            text=text3.get(1.0,END)
            text=text[:10]
            if(str(text) == str(password[17:])):
                self.name=text1.get(1.0,END)
                self.email=text2.get(1.0,END)
                messagebox.showinfo("Successfully Registered","Welcome to our Application")
                submit_button.place(x=670,y=570)
            else:
                messagebox.showerror("Invalid otp","Please enter the Correct OTP")
                text3.delete(1.0,END)
                ok=messagebox.askretrycancel("Resend OTP","Are you sure?")
                
                if ok:
                    send_email()

        def send_email():
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("arun1772003@gmail.com", "vnfntyifwsutzrss")
            global password
            password=generate_otp()
            send_email=str(text2.get(1.0,END))
            s.sendmail("arun1772003@gmail.com",send_email,password)
            s.quit()                            
        def generateID():
            st="AshmapID"
            coll="0123456789"
            for i in range(3):
                st+=coll[random.randrange(0,len(coll),3)]
            return st    
                   
        main=customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
                                 
        customtkinter.set_appearance_mode("dark")
        bg=customtkinter.CTkImage(dark_image=Image.open("images/backu1.png"),size=(1380,720))

        back_img=customtkinter.CTkLabel(self.root,image=bg,text="",fg_color="#111").place(relx=0.5,rely=0.5,anchor=CENTER)     
        fr_color="#111"
        frame=customtkinter.CTkFrame(self.root,width=750,height=400,border_color="yellow",fg_color=fr_color,border_width=10).place(x=350,y=130,anchor=NW)
        
        label1=customtkinter.CTkLabel(self.root,text="Username  :  ",text_color="White",font=("Consolas",23,"bold"),fg_color=fr_color).place(x=470,y=210)
        
        label2=customtkinter.CTkLabel(self.root,text="Email     :  ", text_color="white",font=("Consolas",23,"bold"),fg_color=fr_color).place(x=470,y=300)
        
        label3=customtkinter.CTkLabel(self.root,text="Enter OTP :  ",text_color="white",font=("COnsolas",23,"bold"),fg_color=fr_color).place(x=470,y=390)

        text1=Text(self.root,font=("Consolas",20,"bold"),bg="black",fg="yellow",relief=GROOVE,wrap=WORD)
        text1.place(x=630,y=200,width=350,height=32)

        text2=Text(self.root,font=("Consolas",20,"bold"),bg="black",fg="yellow",relief=GROOVE,wrap=WORD)
        text2.place(x=630,y=290,width=350,height=32)

        text3=Text(self.root,font=("Consolas",20,"bold"),bg="black",fg="yellow",relief=GROOVE,wrap=WORD)
        text3.place(x=630,y=380,width=350,height=32)

        get_button=customtkinter.CTkButton(self.root,text="Generate OTP",command=validate_email,font=("Consolas",15,"bold"),text_color="white",fg_color="red",hover_color="green",
        corner_radius=8).place(x=740,y=342)

        verify_button=customtkinter.CTkButton(self.root,text="Verify OTP",command=verify_otp,font=("Consolas",15,"bold"),text_color="white",fg_color="red",hover_color="green",
        corner_radius=8).place(x=740,y=432)
        
        submit_button=customtkinter.CTkButton(self.root,text="submit",command=GetPermissionImage,font=("Consolas",35,"bold"),text_color="white",fg_color="green",hover_color="orange",
        corner_radius=8)
        
class GetPermissionImage:
    
    def __init__(self):
        self.root=root
        for i in self.root.winfo_children():
            i.destroy()
        customtkinter.set_appearance_mode("dark")
        
        T=customtkinter.CTkTextbox(self.root,width=1200,height=450,font=("Consolas",17,"bold"))
        fact="\nDear Customer,\n\n\tIt's an AI based medical cosultant Application. The predition of the machine sometimes givs us the wrong information . so ,we can use only for checking if your are suffering any pain or any diesease , don't waste your time.Immediately consult your doctor befort getting the big problem\n\n\nsome instructions to \" How to use our Application\" \n\n1 . Click on the first button to speak about your symptoms or health condition.\n2 . Once you have provided the necessary details, click on the Second button to get information about the dieases through speech\n3 . Click on the third button to get the prescription in a PDF format, which will be sent to your registered email\n\t\t\n Note:\n\t The application uses AI to provide a diagnosis, but it is not always accurate. Always consult a doctor if you are experiencing pain or any other health-related issues." 
        T.place(x=100,y=100)
        T.insert(tk.END,fact)
        accpt_button=customtkinter.CTkButton(self.root,text="  Accept  ",font=("Consolas",17,"bold"),text_color="white",fg_color="red",hover_color="green",command=SpeechRecongnition).place(x=970,y=500)
        
        ignore_button=customtkinter.CTkButton(self.root,text="  Ignore  ",font=("Consolas",17,"bold"),text_color="white",fg_color="red",hover_color="green",command=root.destroy).place(x=1130,y=500)
    
class SpeechRecongnition:
   
    def __init__(self):
        self.root=root
        for i in self.root.winfo_children():
            i.destroy() 
            
        customtkinter.set_appearance_mode("dark")
        
        bg=customtkinter.CTkImage(dark_image=Image.open("images/backu2.png"),size=(1380,720))

        back_img=customtkinter.CTkLabel(root,image=bg,text="",fg_color="#111").place(relx=0.5,rely=0.5,anchor=CENTER)

        doc_bg=customtkinter.CTkImage(dark_image=Image.open("images/robot.png"),size=(300,300))
        
        frame_tot=customtkinter.CTkFrame(root,width=700,height=600,border_color="red",border_width=8,fg_color="#111").place(relx=0.5,rely=0.5,anchor=CENTER)

        frame_doc=customtkinter.CTkFrame(root,width=320,height=320,border_color="yellow",border_width=10).place(x=700,y=250,anchor=CENTER) 
        
        doc_label=customtkinter.CTkLabel(frame_doc,image=doc_bg,text="").place(x=700,y=250,anchor=CENTER)

        doc_button = customtkinter.CTkButton(master=root,text="      Tell me what You Feel      ",width=200,height=45,corner_radius=8,font=("Consolas",17,"bold"),hover_color="red",fg_color="green",text_color="white",command=self.speech_symptoms,state=NORMAL).place(x=700,y=450,anchor=CENTER)

        pres_button= customtkinter.CTkButton(master=root,text="       Prescription Advices       ",width=80,height=45,corner_radius=8,font=("Consolas",17,"bold"),hover_color="red",fg_color="green",text_color="white",command=GetDataFromDB,state=NORMAL).place(x=700,y=520,anchor=CENTER)
        
        view_report=customtkinter.CTkButton(master=root,text="        Get Your Reports        ",width=80,height=45,corner_radius=8,font=("Consolas",17,"bold"),hover_color="red",fg_color="green",text_color="white",command=SendingReport,state=NORMAL).place(x=700,y=590,anchor=CENTER)
        
        btn=customtkinter.CTkButton(root,text=" Finish ",fg_color="red",font=("Consolas",17,"bold"),text_color="white",corner_radius=8,hover_color="green",command=root.destroy).place(relx=0.9,rely=0.9,anchor=CENTER)
    
            
    def speech_symptoms(self):
        
        recognizer=spr.Recognizer()
        global result
        with spr.Microphone() as source: 
            print('Clearing background noise...')
            recognizer.adjust_for_ambient_noise(source,duration=1)
            print('Waiting for message..') 
            t.sleep(1)
            audio = recognizer.listen(source,timeout=1)
            print('Done recording..') 
        try:
            print('Recognizing..')
            Dt.result = recognizer.recognize_google(audio,language='en')
            print(Dt.result)
        except Exception as ex:
            messagebox.showerror("Noise Error","I can't hear your voice")
          
class GetDataFromDB():
    
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Prakash@17",
            database="miniproject"
        )
        self.cursor= mydb.cursor()
        self.getDieases(self.cursor)     
        
    def speech(self):   
        for st in Dt.details:
            engine=pyttsx3.init()
            engine.say(st)
            engine.runAndWait()
            
    def getDieases(self,cursor):
        
        self.cursor=cursor
        self.dataDB=[]
        self.cursor.execute('select dieases from patients')
        cur=self.cursor.fetchall()
       
        for i in cur:
            self.dataDB.append(str(i[0]))
        for item1 in self.dataDB:
            if item1 in Dt.result:
                Dt.dieases.append(item1)
        for i in Dt.dieases:
            self.cursor.execute("select * from patients where dieases =\'"+i+"\'")
            for j in self.cursor.fetchall():
                Dt.details.append(j[1])
                Dt.causes.append(j[2])
                Dt.treatment.append(j[3])  
        self.speech()
           

class SendingReport():
    
    def __init__(self):
      
        self.dieasesName=self.getString(Dt.dieases)
        self.treatmentName=self.getString(set(Dt.treatment))
        self.causesName=self.getString(Dt.causes)
        self.detailsName=""
        for i in Dt.details:
            self.detailsName+="\t\t\t\t"+i+"\n"
        self.generateReport()
        self.sendEmailReport()
       
    def getString(self,str):
        self.str=""
        for i in str:
            self.str+=i+' , '
        return self.str[:len(self.str)]
    def sendEmailReport(self):                 
        sender_mail="arun1772003@gmail.com"
        receiver_mail=Dt.personal[2]
        sender_password="vnfntyifwsutzrss"
        subject_of_mail="Your Medical Reports"
        body="Your Medical Report send by Voice based medical consultant Application that was developed by M.Arunprakash"
        filename=Dt.personal[0][0:len(Dt.personal[0])-1]
        location="C:\\Users\\ELCOT\\Desktop\\project folder\\python\\translator\\NewThing"

        k=sendpdf(sender_mail,receiver_mail,sender_password,subject_of_mail,body,filename,location)
        k.email_send()


    def generateReport(self):
        
        pdf=FPDF('P',"mm",'A4')
        pdf.add_page()
        pdf.set_font("Arial",'B',27)
        pdf.image('images/robot.png',5,5,20)
        #BIU,b=bold,i=italic,u=underline
        pdf.set_text_color(220,50,50)
        pdf.ln(5)
        pdf.cell(0,0,txt="Patients Report",align='C')
        pdf.set_line_width(2)
        pdf.ln(13)
        pdf.set_text_color(0,255,0)
        pdf.cell(0,0,txt="",border=True,ln=1)
        pdf.ln(20)
        pdf.set_font("times",'B',16)

        #---------------for name ------------
        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,0,txt="Name ",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,0,txt=":",ln=0,align='C')
        pdf.cell(0,0,txt=Dt.personal[0],ln=1,align='L')
        pdf.ln(13)

        #----------------patient Id------------
        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,0,txt="Patient ID ",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,0,txt=":",ln=0,align='C')
        pdf.cell(0,0,txt=str(Dt.personal[1]),ln=1,align='L')
        pdf.ln(13)

       
        # ----------------------- Dieases ------------------------------
        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,5,txt="Dieases",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,5,txt=":",ln=0,align='C')
        pdf.set_font("times",'B',16)
        pdf.multi_cell(120,6,txt=self.dieasesName)
        pdf.ln(5)

        # ----------------------- Details ------------------------------
        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,5,txt="Details",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,5,txt=":",ln=0,align='C')
        pdf.set_font("times",'B',16)
        pdf.multi_cell(120,6,txt=self.detailsName)
        pdf.ln(8)

        #---------------------------- Causes ---------------------------
        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,5,txt="Causes ",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,5,txt=":",ln=0,align='C')
        pdf.set_font("times",'B',16)
        pdf.multi_cell(120,6,txt=self.causesName)
        pdf.ln(5)

        #----------------Treatment----------------

        pdf.set_x(20)
        pdf.set_text_color(220,50,50)
        pdf.cell(50,5,txt="Treatment Details ",ln=0,align='L')
        pdf.set_text_color(0,255,0)
        pdf.cell(15,5,txt=":",ln=0,align='C')
        pdf.set_font("times",'B',16)
        pdf.multi_cell(180,6,txt=self.treatmentName)
        pdf.ln(13)
        pdf.output(Dt.personal[0][:len(Dt.personal[0])-2]+".pdf")
       
            
root = customtkinter.CTk()
Dt = UserData()
Login(root)
root.mainloop()   

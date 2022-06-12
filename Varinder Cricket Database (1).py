
file1=""
vidpath = ""
document1=""

import mysql.connector as mysql
import tkinter as tk, threading
from PIL import Image, ImageTk
import PIL.Image
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
from tkVideoPlayer import TkinterVideo

window= Tk()
window.title("Cricketers")
window.geometry("700x500")
window.configure(background="white")
window.option_add( "*font", "lucida 12 bold " )

mydb= mysql.connect(host="localhost",user="root",passwd="dhillon",database="cricket_data")

myfont = ("lucida 14 bold")

mydb= mysql.connect(host="localhost",user="root",passwd="dhillon",database="cricket_data")
cursor = mydb.cursor()



def making_table():

    try:
        
        cursor.execute("create table player(jersey_no int primary key,player_name varchar(50),born date,height float,role varchar(50),playing_style varchar(50),doc_address varchar(100), vid_address varchar(100));")
        cursor.execute("commit");

    except:
        pass
    
making_table()


def streaming(vidpath):
    
    try:
        
        videoplayer = TkinterVideo(master=window, scaled=False, pre_load=False)
        videoplayer.set_size((500,300))
        videoplayer.load(vidpath)
        videoplayer.place(x=750,y=300)
        videoplayer.play()
    
    except :
        pass

def opendocfile():


    global document1
    e_doc_address.delete(0,'end')
    filename=filedialog.askopenfilename(filetypes=(("doc files","*.docx"),("All Files","*.*")))
    document1 = filename
    e_doc_address.insert(0,document1)


def vid_add():

    global vidpath
    e_vid_address.delete(0,'end')
    filename = filedialog.askopenfilename(filetypes=(("doc files","*.docx"),("All Files","*.*")))
    vidpath = filename
    e_vid_address.insert(0,vidpath)

def clear():

                        ejersey.delete('0','end')
                        ename.delete('0','end')
                        eborn.delete('0','end')
                        eheight.delete('0','end')
                        erole.delete('0','end')
                        estyle.delete('0','end')
                        e_doc_address.delete('0','end')
                        e_vid_address.delete('0','end')
                        for_list()

                        ejersey.focus_set()
                        
                        x="patch1.png"
                        img = PIL.Image.open(x)
                        img = img.resize((600,700), PIL.Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label( image=img)
                        panel.image = img
                        panel.place(x=700,y=5)
                        window.geometry("700x500")
                        
def details():


        try:
      
                jersey= ejersey.get()
                name= (ename.get())
                born = (eborn.get())
                height= (eheight.get())
                role= (erole.get())
                style= (estyle.get())
                doc_address = e_doc_address.get()
                vid_address = e_vid_address.get()

                if jersey=="" or name=="" or role=="":
                    tk.messagebox.showinfo("Enter Values","All Values Are Neccesary")
                else :    
                    cursor.execute("insert into player values("+ jersey +",'"+ name +"','"+ born +"','"+ height +"','"+ role +"','"+ style +"','"+ doc_address +"','"+ vid_address +"');")
                    mydb.commit()
                    tk.messagebox.showinfo("Success","Data Added Successfully")
        
                ejersey.delete('0','end')
                ename.delete('0','end')
                eborn.delete('0','end')
                eheight.delete('0','end')
                erole.delete('0','end')
                estyle.delete('0','end')
                e_doc_address.delete('0','end')
                e_vid_address.delete('0','end')

                ejersey.focus_set()
                for_list()
                
        except mysql.connector.errors.IntegrityError:
                tk.messagebox.showinfo("Error","Jersey No. Already Exists")
                

def show_document():


    global document1
    x= document1
    img = PIL.Image.open(x)
    img = img.resize((200,200), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.place(x=900,y=60)

    
    ejersey.focus_set()

def show():

        try:      
                global file1
                global document1
                
                no = ejersey.get()
                if no=="":
                        tk.messagebox.showinfo("Error","Jersey No. is needed")
                else:
                        cursor.execute("select * from player where jersey_no = "+ no +"")
                        x1=cursor.fetchall()
                        count=cursor.rowcount
                        if count==0:
                                tk.messagebox.showinfo("--No data found")
                        else:
                                clear()
                                for x in x1:
                                        ejersey.insert(0,x[0])
                                        ename.insert(0,x[1])
                                        eborn.insert(0,x[2])
                                        eheight.insert(0,x[3])
                                        erole.insert(0,x[4])
                                        estyle.insert(0,x[5])
                                        e_doc_address.insert(0,x[6])
                                        e_vid_address.insert(0,x[7])
                                        document1 = x[6]
                                        vidpath = x[7]
                                window.geometry("1300x800")       
                                show_document()
                                thread = threading.Thread(target=streaming, args=(vidpath,))
                                thread.daemon = True
                                thread.start()
        except:
                    pass

def update():
     

                no = ejersey.get()
                if no=="":
                        tk.messagebox.showinfo("Error","Jersey No. is neccessary for updating")
                else:
                        jersey= ejersey.get()
                        name= (ename.get())
                        born = (eborn.get())
                        height= (eheight.get())
                        role= (erole.get())
                        style= (estyle.get())
                        doc_address = e_doc_address.get()
                        vid_address = e_vid_address.get()
                        
                        cursor.execute("update player set jersey_no= "+ jersey +",player_name='"+ name +"',born='"+ born +"',height='"+ height +"',role='"+ role +"',playing_style='"+ style +"',doc_address='"+doc_address +"',vid_address='"+ vid_address +"' where jersey_no = "+ no +";")
                        mydb.commit()
                        tk.messagebox.showinfo("Success","Data Updated Successfully")
                        ejersey.delete('0','end')
                        ename.delete('0','end')
                        eborn.delete('0','end')
                        eheight.delete('0','end')
                        erole.delete('0','end')
                        estyle.delete('0','end')
                        e_doc_address.delete('0','end')
                        e_vid_address.delete('0','end')
                        for_list()

                        ejersey.focus_set()


                        
def delete():

    
       
                no = ejersey.get()
                if no=="":
                        tk.messagebox.showinfo("Error","Jersey No. is neccessary for deletion")
                else:
                        cursor.execute("delete from player where jersey_no="+no+"")
                        mydb.commit()
                        tk.messagebox.showinfo("success","Data deleted Successfully")
                        ejersey.delete('0','end')
                        ename.delete('0','end')
                        eborn.delete('0','end')
                        eheight.delete('0','end')
                        erole.delete('0','end')
                        estyle.delete('0','end')
                        e_doc_address.delete('0','end')
                        e_vid_address.delete('0','end')

                        ejersey.focus_set()

                        x="patch1.png"
                        img = PIL.Image.open(x)
                        img = img.resize((600,700), PIL.Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label( image=img)
                        panel.image = img
                        panel.place(x=700,y=5)
                        window.geometry("700x500")

                        
def adding_pictures():

    x="icc.png"
    img = PIL.Image.open(x)
    img = img.resize((100, 100), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.place(x=50,y=10)
    x="IPL.JPG"
    img = PIL.Image.open(x)
    img = img.resize((100,100), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.place(x=450,y=10)

adding_pictures()


def for_list():
        
        con= mysql.connect(host="localhost",user="root",password="dhillon",database="cricket_data")
        cursor=con.cursor()
        cursor.execute("select * from player")
        rows=cursor.fetchall()
        list.delete(0,list.size())
        
        for row in rows:
            insertData=str(row[0])+' - '+row[1]
            list.insert(list.size()+1,insertData)
       
        
        con.close()


    
Label(text="Cricket Database",font= ("lucida 20 bold"),bg="#f96167",fg="#FCE77D").place(x=200,y=30)         

label_jersey=Label(text="Jersey No.",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=120)

label_name= Label(text="Player Name",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=160)

label_born= Label(text="Born",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=200)

label_height= Label(text="Height",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=240)

label_role= Label(text="Role",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=280)

label_style= Label(text="Playing Style",font=myfont,bg="#eb2188",fg="#080a52").place(x=50,y=320)

#entry field
ejersey=Entry(font=("lucida 12 bold"))
ejersey.place(x=200,y=120)

ename=Entry(font=("lucida 12 bold"))
ename.place(x=200,y=160)

eborn =Entry(font=("lucida 12 bold"))
eborn.place(x=200,y=200)

eheight=Entry(font=("lucida 12 bold"))
eheight.place(x=200,y=240)

erole=Entry(font=("lucida 12 bold"))
erole.place(x=200,y=280)

estyle=Entry(font=("lucida 12 bold"))
estyle.place(x=200,y=320)

e_doc_address = Entry(font=("lucida 12 bold"))
e_doc_address.place(x=200,y=360)

e_vid_address = Entry(font=("lucida 12 bold"))
e_vid_address.place(x=200,y=400)

#getting values
Button(text="Submit",bg="#050505",fg="white",command=details).place(x=50,y=440)

Button(text="Clear",bg="#ffcccb",fg="black",command=clear).place(x=130,y=440)

Button(text="Delete",bg="#050505",fg="white",command=delete).place(x=350,y=440)

Button(text="Show",bg="#050505",fg="white",command=show).place(x=200,y=440)

Button(text="Update",bg="#ffcccb",fg="black",command=update).place(x=270,y=440)

Button(text="Video Path",command= vid_add,bg="#eb2188",fg="#080a52").place(x=50,y=400)

opendocfile=Button(text="Player info place",font=("lucida 12 bold"),bg="#eb2188",fg="#080a52",command=opendocfile)
opendocfile.place(x=50,y=360)

ejersey.focus_set()

window.bind('<Return>',lambda event:show())

list=Listbox(height=13,width=25)
list.place(x=435,y=120)

for_list()


window.mainloop()

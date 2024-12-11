from tkinter import *
from gtts import gTTS
from playsound import playsound
def myfun1():
    exit()
def myfun2():
    tex=mytext.get()
    mysound=gTTS(text=tex)
    mysound.save('textplay.mp3')
    playsound('textplay.mp3')
def myfun3():
    mytext.delete(0,END)    
frame=Tk()
frame.title("Text to speech")
frame.geometry("500x300")
mylabel1=Label(frame,text="Text to speech",font="Tahoma 30 bold",fg="#1c1730").pack(pady=10)
mylabel2=Label(frame,text="Enter your text:-",font="Georgia 20 bold")
mylabel2.pack(anchor="nw",pady=5)
mytext=Entry(frame,width=50)
mytext.pack(anchor="nw",padx=5,ipady=5)
mybutton1=Button(frame,text="Play",fg="black",bg="green",font="Georgia 10 bold",command=myfun2)
mybutton1.pack(side="left",padx=10,pady=10,anchor="nw",ipadx=10,ipady=5)
mybutton2=Button(frame,text="set",fg="black",bg="blue",font="Georgia 10 bold",command=myfun3)
mybutton2.pack(side="right",padx=10,pady=10,anchor="ne",ipadx=10,ipady=5)
mybutton3=Button(frame,text="Exit",fg="black",bg="red",font="Georgia 10 bold",command=myfun1)
mybutton3.pack(pady=10,ipadx=10,ipady=5)
frame.mainloop()
import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os




# Initialisation de la fenêtre principale
root = Tk()
root.title("Text to speech")
root.geometry("900x500+100+100")
root.resizable(False,False)
root.configure(bg="#305065")


# Initialisation de pyttsx3
engine = pyttsx3.init('sapi5')

# Récupérer les voix et les langues
voices = engine.getProperty('voices')






 

def speaknow():
    text_content = Text_area.get(1.0,END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        for voice in voices:
            engine.setProperty('voice', voice.id)
         
        #if(gender == 'Male'):
            #engine.setProperty('voice', voices[0].id)
        #else:
          #  engine.setProperty('voice', voices[1].id)
       
            engine.say(text_content)
        engine.runAndWait()
      
            
            
    if (text_content):
        if (speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()



def download():
   text_content = Text_area.get(1.0,END)
   gender = gender_combobox.get()
   speed = speed_combobox.get()
   voices = engine.getProperty('voices')
    
   def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text_content, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text_content, 'text.mp3')
            engine.runAndWait()
   if (text_content):
        if (speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()








#icon
image_icon =PhotoImage(file= "speak.png")
root.iconphoto(False, image_icon)



#Top frame
top_frame = Frame(root, bg="white", width=900,height=100)
top_frame.place(x=0,y=0)


logo = PhotoImage(file="speaker_logo.png")
Label(top_frame,image=logo,bg="white").place(x=10,y=5)
Label(top_frame, text="Text To Speech", font="arial 20 bold", bg="white",fg="black").place(x=100,y=40)

# Zone de texte
Text_area = Text(root, font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
Text_area.place(x=10,y=120,width=500,height=250)


# Labels pour VOICE et SPEED

Label(root,text="VOICE", font="arial 15 bold",bg="#305065", fg="white").place(x=580,y=160)
Label(root,text="SPEED", font="arial 15 bold",bg="#305065", fg="white").place(x=760,y=160)



# Combobox pour le genre
gender_combobox = Combobox(root, values = ['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')




# Combobox pour la vitesse
speed_combobox = Combobox(root, values = ['Fast', 'Normal', 'slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')




# Bouton Speak
image_icon  = PhotoImage(file= "speak.png")
btn = Button(root, text="Speak",compound=LEFT,width=130,image=image_icon,font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)




# Bouton Save
image_icon2  = PhotoImage(file= "download.png")
save = Button(root, text="save",compound=LEFT,image=image_icon2,bg="#39c790",width=130,font="arial 14 bold", command=download)
save.place(x=730, y=280)











root.mainloop()


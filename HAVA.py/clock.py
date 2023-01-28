from tkinter import *
from time import *

def update():
    global timeString 
    timeString = strftime("%I:%M:%S")
    timeLabel.config(text=timeString)
    timeLabel.after(1000,update)

window = Tk()
window.title("Clock")

timeLabel = Label(window,font=("Helvetica",50,"bold"),fg="#00FF00",bg="black")
timeLabel.pack()

update()

window.mainloop()
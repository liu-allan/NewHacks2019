import tkinter
import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import serial
import subprocess

global count
count = 0
global btn_search_2

#database of the plants' water needed for each stage of growth
plants = {
    "Alfalfa": [800, 1600],
    "Banana": [1200, 2200],
    "Barley": [450, 650],
    "Oats": [450, 650],
    "Wheat": [450, 650],
    "Bean": [300, 500],
    "Cabbage": [350, 500],
    "Citrus": [900, 1200],
    "Cotton": [700, 1300],
    "Maize": [500, 800],
    "Melon": [400, 600],
    "Onion": [350, 550],
    "Peanut": [500, 700],
    "Pea": [350, 500],
    "Pepper": [600, 900],
    "Potato": [500, 700],
    "Sorghum": [450, 650],
    "Millet": [450, 650],
    "Soybean": [450, 700],
    "Sugarbeet": [550, 750],
    "Sugarcane": [1500, 2500],
    "Sunflower": [600, 1000],
    "Tomato": [400, 800]
}

#declaring a root GUI that allows the user to select the plant type as well as the stage in growth
root = tkinter.Tk()
root.title("Plant and Stage of Growth Selector")
root.state('zoomed')

#function that prompts the user for inputs
def input_change():

    input = (user_input_2.get())

    if input in plants:
        global maxWater
        maxWater = plants[input]
        print(maxWater)

        user_input_3 = Label(root, text="Seed/Mature")
        user_input_3.grid(row=1, column=0)
        user_input_3.config(font=('helvetica', 50))
        user_input_2.delete(0, 'end')

        input_change_2()

    else:
        messagebox.showinfo("Error", "No valid plant, try again")
        user_input_2.delete(0, 'end')

def btn_search():
   input_change()

def input_change_2():
    global user_input_4
    user_input_4 = tkinter.Entry(root, bd=5)
    user_input_4.grid(row=1, column=1)
    user_input_4.config(font=('helvetica', 50))

    search = tkinter.Button(root, text="Search", command=btn_search_2)
    search.grid(row=2, column=0, columnspan=2)
    search.config(bg='green', fg='white', font=('helvetica', 50))

#function that prompts the user to enter the stage level of their plant
def btn_search_2():
    stage = (user_input_4.get())
    if stage == "Seed":
        plantAge = maxWater[0]
        print(plantAge)
        root.destroy()
    elif stage == "Mature":
        plantAge = maxWater[1]
        print(plantAge)
        root.destroy()
    else:
        messagebox.showinfo("Error", "Invalid input, try again")
        user_input_4.delete(0, 'end')

#declaring all the images and entries and searches buttons
pic_sunflowers = ImageTk.PhotoImage(Image.open('C:/Users/aa123/Desktop/Sunflowers.jpg').resize((600, 600), Image.ANTIALIAS))
panel_sunflowers = tkinter.Label(root, image= pic_sunflowers)
panel_sunflowers.grid(row=0,column=0)

pic_plants = ImageTk.PhotoImage(Image.open('C:/Users/aa123/Desktop/Plants.jpg').resize((600, 600), Image.ANTIALIAS))
panel_plants = tkinter.Label(root, image= pic_plants)
panel_plants.grid(row=0,column=1)

user_input_1=Label(root,text="Enter a plant")
user_input_1.grid(row=1,column=0)
user_input_1.config(font=('helvetica',50))

user_input_2 = tkinter.Entry(root, bd=5)
user_input_2.grid(row=1,column=1)
user_input_2.config(font=('helvetica',50))

search = tkinter.Button(root, text="Search",command = btn_search)
search.grid(row=2,column=0,columnspan=2)
search.config(bg='green',fg='white', font=('helvetica',50))

root.mainloop()

global alreadySound
alreadySound = FALSE

#subsequent to the completion of user inputs, the program will then display a panel for the current water level
base = tkinter.Tk()
base.title("Current Water Level Display")
base.state('zoomed')

text = tkinter.Text(base)
text.insert(INSERT, "STANDBY")
text.pack()
text.config(bg='green', font=('helvetica',200))

#if at any point the water level is beyond 600, the program will emit a sound alert to notify the user to stop watering the plant
#then, if at any point the water level is below 300, the program will first allow the user to pour in some water. If no action has been
#taken, the program will send an alert to the user's phone. If the user begins to pour water and the water exceeds the maximum amount of water
#needed, the program will emit a sound alert.
def verify():
    arduino = serial.Serial('COM10', 115200)
    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    data_final = (data.decode('utf-8'))
    print(data_final)
    base.after(1,verify)

    global alreadySound
    if alreadySound == FALSE:
        if data_final>'600':
            import winsound
            duration = 3000
            freq = 750
            winsound.Beep(freq, duration)
            print("TOO MUCH WATER")
            alreadySound = TRUE

    if data_final<'300':
        time.sleep(8)
        data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
        data_final = (data.decode('utf-8'))
        if data_final<'300':
            base.destroy()

base.after(1000,verify)

base.mainloop()

#IMPORTANT NOTE: PLEASE COMMENNT THE LAST TWO LINES OUT WHEN JUDGES ARE TESTING THE CODE (it'll continually send one of the group
#member text messages, thank you very much!)
print("ADD SOME WATER")
theproc = subprocess.Popen("python send_sms.py", shell = True)
theproc.communicate()
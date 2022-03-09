import requests
from tkinter import *

req = requests.get("https://api.ipify.org?format=json")
ip = req.json()["ip"]
print(ip)

ablak1 = Tk()
ablak1.title("IKT Projekt - Zoltán nap")
ablak1.geometry('500x700')
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\favicon.png")
ablak1.config(background="white")
ablak1.iconphoto(True, icon)
kep1 = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\xy.gif")

cimke = Label(ablak1, 
        text=ip, 
        fg="#000000",
        font=("Comic Sans MS", 35, "bold"),
        bd=10,
        padx=25,
        pady=10,
        image = kep1,
        compound="bottom").pack()
gomb1 = Button(ablak1,
            text= "Ratio 🗿",
            bg= "#ffffff",
            fg= "#bbbbbb",
            font= ("Impact", 10),
            bd=10,
            padx = 5,
            pady = 2,
            compound = "left",
            activebackground = "#ffffff",
            activeforeground = "#ffffff",
            relief = "flat")
gomb1.pack(pady = 20)
ablak1.mainloop()
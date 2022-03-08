from tkinter import *
ablak1 = Tk()
ablak1.title("IKT Projekt - Zoltán nap")
ablak1.geometry('450x500')
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\favicon.png")
ablak1.config(background="black")
ablak1.iconphoto(True, icon)
kep1 = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\xy.gif")

cimke = Label(ablak1, 
        text="25.30.242.124", 
        fg="#000000",
        font=("Comic Sans MS", 35, "bold"),
        bd=10,
        padx=25,
        pady=10,
        image = kep1,
        compound="bottom").pack()

ablak1.mainloop()
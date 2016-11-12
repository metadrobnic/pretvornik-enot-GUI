import Tkinter
import tkMessageBox
from random import randint

window = Tkinter.Tk()

pozdrav = Tkinter.Label(window, text="Vnesi stevilo kilometrov")
pozdrav.pack()   #to zapakira zgornjo vrstico in pokaze text v windowu

vpisno_okno = Tkinter.Entry(window)
vpisno_okno.pack()


def pretvornik():
    vpisani_km = int(vpisno_okno.get())
    milje = vpisani_km * 1.6

    tkMessageBox.showinfo("Your guess result", milje)


check_button = Tkinter.Button(window, text="Check", command=pretvornik)
check_button.pack()

window.mainloop()





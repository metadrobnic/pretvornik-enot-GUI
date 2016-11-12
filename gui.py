import Tkinter
import tkMessageBox
from random import randint


skrita_stevilka = randint (1, 10)

print(skrita_stevilka)


window = Tkinter.Tk()  #to je pojavno okno

pozdrav = Tkinter.Label(window, text="Ugani skrito stevilko")
pozdrav.pack()   #to zapakira zgornjo vrstico in pokaze text v windowu

vpisno_okno = Tkinter.Entry(window)
vpisno_okno.pack()


def preveri_stevilko():
    ugibano_stevilo = int(vpisno_okno.get())
    if ugibano_stevilo < skrita_stevilka:
        alert_text = "Prenizka stevilka"
    elif ugibano_stevilo == skrita_stevilka:
        alert_text = "Uganil si"
    else:
        alert_text = "Previsoka stevilka"

    tkMessageBox.showinfo("Your guess result", alert_text)

check_button = Tkinter.Button(window, text="Check", command=preveri_stevilko)
check_button.pack()

window.mainloop()

print("sedaj sem tukaj")
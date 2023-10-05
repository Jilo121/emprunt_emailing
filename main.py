import tkinter as tk
from tkinter import ttk
from funBank import *

# ------------------ create windows -------------------------

window = tk.Tk()
window.title("Alert client")
window.geometry("1200x600")

# ------------------ add theme -------------------------

style = ttk.Style(window)
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# ------------------ frame principale -------------------------

frame = tk.Frame()
frame.pack()

# ------------------ frame label -------------------------

left_frame = ttk.Frame(frame)
left_frame.grid(row=0, column=0)

right_frame = ttk.Frame(frame)
right_frame.grid(row=0,column=1)

# ------------------ Content -------------------------

info_peso_titre = ttk.Label(left_frame,text="INFORMATION PERSONNELLE:", font=("Arial", 20))
info_peso_titre.grid(row=0,columnspan=2) # columnspan : combiner n column

name_label = ttk.Label(left_frame, text="NOM :", width=15)
name_label.grid(row=1,column=0,padx=10)

name_entry = ttk.Entry(left_frame)
name_entry.grid(row=1,column=1,padx=10,pady= 5)

lastname_label = ttk.Label(left_frame, text="PRENOM :", width=15)
lastname_label.grid(row=2,column=0,padx=10, )

lastname_entry = ttk.Entry(left_frame)
lastname_entry.grid(row=2,column=1,padx=10,pady= 5)

email_label = ttk.Label(left_frame, text="EMAIL :", width=15)
email_label.grid(row=3,column=0,padx=10, )

email_entry = ttk.Entry(left_frame)
email_entry.grid(row=3,column=1,padx=10,pady= 5)

contact_label = ttk.Label(left_frame, text="CONTACTE :", width=15)
contact_label.grid(row=4,column=0,padx=10, )

contact_entry = ttk.Entry(left_frame)
contact_entry.grid(row=4,column=1,padx=10,pady= 5)


window.mainloop()
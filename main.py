import tkinter as tk
from tkinter import ttk
from funBank import *

# ------------------ create windows -------------------------

window = tk.Tk()
window.title("Alert client")
# window.geometry("900x750")
window.minsize(1200, 800)
# window.maxsize(1200, 800)

# ------------------ add theme -------------------------

style = ttk.Style(window)
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# ------------------ frame principale -------------------------

frame = tk.Frame()
frame.pack()

# ------------------ frame label -------------------------

top_frame = ttk.Frame(frame)
top_frame.grid(row=0, column=0)

btm_frame = ttk.Frame(frame)
btm_frame.grid(row=1, column=0, pady=20)

right_frame = ttk.Frame(frame)
right_frame.grid(row=0, rowspan=2, column=1, padx=10)
# ------------------ LEFT Content -------------------------

info_peso_titre = ttk.Label(top_frame,text="INFORMATION PERSONNELLE:", font=("Arial", 20))
info_peso_titre.grid(row=0,columnspan=2) # columnspan : combiner n column

name_label = ttk.Label(top_frame, text="NOM :", width=20)
name_label.grid(row=1,column=0,padx=10)

name_entry = ttk.Entry(top_frame, width=30)
name_entry.grid(row=1,column=1,padx=10,pady= 5)

lastname_label = ttk.Label(top_frame, text="PRENOM :", width=20)
lastname_label.grid(row=2,column=0,padx=10, )

lastname_entry = ttk.Entry(top_frame, width=30)
lastname_entry.grid(row=2,column=1,padx=10,pady= 5)

email_label = ttk.Label(top_frame, text="EMAIL :", width=20)
email_label.grid(row=3,column=0)

email_entry = ttk.Entry(top_frame, width=30)
email_entry.grid(row=3,column=1,padx=10,pady= 5)

contact_label = ttk.Label(top_frame, text="CONTACTE :", width=20)
contact_label.grid(row=4, column=0)

contact_entry = ttk.Entry(top_frame, width=30)
contact_entry.grid(row=4, column=1, padx=10, pady=5)

adresse_label = ttk.Label(top_frame, text="ADRESSE :", width=20)
adresse_label.grid(row=5, column=0)

adresse_entry = ttk.Entry(top_frame, width=30)
adresse_entry.grid(row=5, column=1, pady=10)

info_com_titre = ttk.Label(top_frame,text="INFORMATION SUR L'ACTIVITE:", font=("Arial", 20))
info_com_titre.grid(row=6,columnspan=2, pady=30) # columnspan : combiner n column

type_com_label = ttk.Label(top_frame, text="TYPE DE COMMERCE: ", width=20)
type_com_label.grid(row=7, column=0)

type_com_entry = ttk.Entry(top_frame, width=30)
type_com_entry.grid(row=7, column=1, pady=5)

nom_dom_label = ttk.Label(top_frame, text="NOM DE DOMAINE :", width=20)
nom_dom_label.grid(row=8, column=0)

nom_dom_entry = ttk.Entry(top_frame, width=30)
nom_dom_entry.grid(row=8, column=1, pady=10)

activity_label = ttk.Label(top_frame, text="ACTIVITE :", width=20)
activity_label.grid(row=9,column=0)

activity_entry = ttk.Entry(top_frame, width=30)
activity_entry.grid(row=9, column=1, pady=10)

# ------------------ RIGHT Content -------------------------

info_empr_titre = ttk.Label(top_frame,text="DETAIL DE L'EMPRUNT:", font=("Arial", 20))
info_empr_titre.grid(row=10,columnspan=2) # columnspan : combiner n column

type_emp_label = ttk.Label(top_frame, text="TYPE D'EMPRUNT :", width=20)
type_emp_label.grid(row=11, column=0, padx=10)

type_emp_entry = ttk.Combobox(top_frame,value=["Micro", "TPE", "PME", "Akanisoa", "Tranosoa 1", "Tanosoa 2", "Zarasoa"], width=27)
type_emp_entry.grid(row=11, column=1, padx=10, pady=5)

duree_label = ttk.Label(top_frame, text="DUREE :", width=20)
duree_label.grid(row=12, column=0,padx=10, )

duree_entry = ttk.Spinbox(top_frame, width=23, from_=2, to=20)
duree_entry.grid(row=12, column=1,padx=10,pady= 5)

montant_dem_label = ttk.Label(top_frame, text="MONTANT DEMANDER :", width=20)
montant_dem_label.grid(row=13, column=0)

montant_dem_entry = ttk.Entry(top_frame, width=30)
montant_dem_entry.grid(row=13, column=1,padx=10,pady= 5)

date_dem_label = ttk.Label(top_frame, text="DATE D'EMPRUNT :")
date_dem_label.grid(row=14, column=0)

date_entry = ttk.Entry(top_frame, width=30)
date_entry.grid(row=14, column=1,padx=10,pady= 5)


# ------------------ Content BTM-------------------------

rec_btn = ttk.Button(btm_frame, text="Enregistrer", width=20)
rec_btn.grid(row=0, column=0)

clear_btn = ttk.Button(btm_frame, text="Effacer", width=20)
clear_btn.grid(row=0, column=1, padx=10)

update_btn = ttk.Button(btm_frame, text="Mettre à jours", width=20)
update_btn.grid(row=1, column=0, pady=5)

# ------------------ RIGHT FRAME -------------------------


window.mainloop()
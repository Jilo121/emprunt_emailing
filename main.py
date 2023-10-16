import tkinter as tk
from tkinter import ttk
# from funBank import *
import sqlite3
import bdd_Bank
from envoie_email import proc_envoie
# import tkcalendar

# ------------------ create windows -------------------------

window = tk.Tk()
window.title("Alert client")
# window.geometry("900x750")
window.minsize(900, 800)
# window.maxsize(1200, 800)

# ------------------ add theme -------------------------

style = ttk.Style(window)
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# ------------------ frame principale -------------------------

frame = tk.Frame()
frame.pack()

# ------------------ BDD -------------------------

# def insertdonnee():
#     conn = sqlite3.connect('database/information.db')

#     curseur = conn.cursor()
#     conn.execute("INSERT INTO information(name, lastname, email, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem) VALUES('?,?,?,?,?,?,?,?,?,?,?,?')",(name_entry.get(),lastname_entry.get(),email_entry.get(),contact_entry.get(),adresse_entry.get(),type_com_entry.get(),nom_dom_entry.get(),activity_entry.get(),type_emp_entry.get(),duree_entry.get(),montant_dem_entry.get(),date_entry.get()))
#     conn.commit()
#     conn.close()

# ------------------ frame label -------------------------

top_frame = ttk.Frame(frame)
top_frame.grid(row=0, column=0)

btm_frame = ttk.Frame(frame)
btm_frame.grid(row=1, column=0, pady=20)

right_top_frame = ttk.Frame(frame, height=30)
right_top_frame.grid(row=0,rowspan=2, column=1)

right_btm_frame = ttk.Frame(frame)
right_btm_frame.grid(row=1, column=1)

childframe1 = ttk.Frame(right_top_frame)
childframe2 = ttk.Frame(right_top_frame)

childframe1.grid(row=0, column=0)
childframe2.grid(row=1, column=0)

childframe1b = ttk.Frame(right_btm_frame)
childframe2b = ttk.Frame(right_btm_frame)

childframe1b.grid(row=0, column=0)
childframe2b.grid(row=1, column=0)
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

# sel = tk.StringVar()

# cal = tkcalendar.DateEntry(top_frame, selectmode='day', textvariable=sel)
# cal.grid(row=14, column=2, padx=15)

# sel.trace('w', top_frame)

# ------------------ Liste des donnée -------------------------

name_ = name_entry.get()
lastname_ = lastname_entry.get()
email_ = email_entry.get()
contact = contact_entry.get()
adresse = adresse_entry.get()
type_com = type_com_entry.get()
nom_dom = nom_dom_entry.get()
activity = activity_entry.get()
type_emp = type_emp_entry.get()
duree = duree_entry.get()
montant_dem = montant_dem_entry.get()
date_dem = date_entry.get()
id = 5
# ------------------ Content BTM-------------------------

rec_btn = ttk.Button(btm_frame, text="Enregistrer", width=20)
#, command=bdd_Bank.insertdonnee(id,name_, lastname_, email_, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem)
rec_btn.grid(row=0, column=0)

clear_btn = ttk.Button(btm_frame, text="Effacer", width=20)
clear_btn.grid(row=0, column=1, padx=10)

update_btn = ttk.Button(btm_frame, text="Mettre à jours", width=20)
update_btn.grid(row=1, column=0, pady=5)

# ------------------ RIGHT FRAME -------------------------

treescroll = ttk.Scrollbar(childframe1)
treescroll.pack(side="right", fill="y")

# treescroll2 = ttk.Scrollbar(right_top_frame)
# treescroll2.pack(side="bottom", fill="x")

titrepart1 = ttk.Label(childframe1, text="En cours:", font=("Arial", 20))
titrepart1.pack()

# form_scroll = ttk.Scrollbar(top_frame)
# form_scroll.grid(side="right", fill="y")
# treescroll.config(command=top_frame)

treeview= ttk.Treeview(childframe1, height=10) #show="headings"
# column
treeview['columns'] = ("Nom","Email","Adresse","Nom du domaine","Activité","Type d'emprunt","Durée","Date d'emprunt","Montant")
treeview.column("#0", width=20, anchor="w")
treeview.column("Nom", width=150, anchor="w")
treeview.column("Email", width=100, anchor="w")
treeview.column("Adresse", width=200, anchor="w")
treeview.column("Nom du domaine", width=100, anchor="w")
treeview.column("Activité", width=100, anchor="w")
treeview.column("Type d'emprunt", width=100, anchor="w")
treeview.column("Durée", width=100, anchor="w")
treeview.column("Date d'emprunt", width=100, anchor="w")
treeview.column("Montant", width=100, anchor="w")

# heading
treeview.heading("#0", text="Label", anchor="w")
treeview.heading("Nom", text="Nom", anchor="w")
treeview.heading("Email", text="Email", anchor="w")
treeview.heading("Adresse", text="Adresse", anchor="w")
treeview.heading("Nom du domaine", text="Nom du domaine", anchor="w")
treeview.heading("Activité", text="Activité", anchor="w")
treeview.heading("Type d'emprunt", text="Type d'emprunt", anchor="w")
treeview.heading("Durée", text="Durée", anchor="w")
treeview.heading("Date d'emprunt", text="Date d'emprunt", anchor="w")
treeview.heading("Montant", text="Montant", anchor="w")

# ---------------------------- insert data ----------------------------------

donnee = bdd_Bank.prendredonnee()
count = 0
for disp in donnee:
    treeview.insert(parent='', index='end',iid=count,text='', values=(disp[1],disp[3],disp[5],disp[7],disp[8],disp[9],disp[10],disp[11],disp[12]))
    count += 1

treeview.pack()
treescroll.config(command=treeview.yview)
# treescroll2.config(command=treeview.xview)

# ----------------------------------------------------------------- treeview2 data ------------------------------------------------------------------------------------------

tree2label = ttk.Label(childframe2, text="Terminer :", font=("Arial",20))
tree2label.pack()

treeview2= ttk.Treeview(childframe2, height=10) #show="headings"
# column
treeview2['columns'] = ("Nom","Email","Adresse","Nom du domaine","Activité","Type d'emprunt","Durée","Date d'emprunt","Montant")
treeview2.column("#0", width=20, anchor="w")
treeview2.column("Nom", width=150, anchor="w")
treeview2.column("Email", width=100, anchor="w")
treeview2.column("Adresse", width=200, anchor="w")
treeview2.column("Nom du domaine", width=100, anchor="w")
treeview2.column("Activité", width=100, anchor="w")
treeview2.column("Type d'emprunt", width=100, anchor="w")
treeview2.column("Durée", width=100, anchor="w")
treeview2.column("Date d'emprunt", width=100, anchor="w")
treeview2.column("Montant", width=100, anchor="w")

# heading
treeview2.heading("#0", text="Label", anchor="w")
treeview2.heading("Nom", text="Nom", anchor="w")
treeview2.heading("Email", text="Email", anchor="w")
treeview2.heading("Adresse", text="Adresse", anchor="w")
treeview2.heading("Nom du domaine", text="Nom du domaine", anchor="w")
treeview2.heading("Activité", text="Activité", anchor="w")
treeview2.heading("Type d'emprunt", text="Type d'emprunt", anchor="w")
treeview2.heading("Durée", text="Durée", anchor="w")
treeview2.heading("Date d'emprunt", text="Date d'emprunt", anchor="w")
treeview2.heading("Montant", text="Montant", anchor="w")

#--------------------------------------------- insert data --------------------------------------------------
donnee = bdd_Bank.prendredonnee()
count = 0
print(donnee)
for disp in donnee:
    treeview2.insert(parent='', index='end',iid=count,text='', values=(disp[1],disp[3],disp[5],disp[7],disp[8],disp[9],disp[10],disp[11],disp[12]))
    count += 1
treeview2.pack()

window.mainloop()
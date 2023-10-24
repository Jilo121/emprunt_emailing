import tkinter as tk
from tkinter import ttk
import sqlite3
from send_email import lancerproc
from threading import Thread

# ------------------ create windows -------------------------

def createTable():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("""CREATE TABLE IF NOT EXISTS information (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL, 
                        lastname TEXT NOT NULL, 
                        email TEXT NOT NULL, 
                        contact	TEXT NOT NULL, 
                        adresse	TEXT NOT NULL,
                        type_com	TEXT NOT NULL,
                        nom_dom	TEXT NOT NULL,
                        activity TEXT NOT NULL, 
                        type_emp	TEXT NOT NULL, 
                        duree INTEGER NOT NULL,
                        montant_dem	INTEGER NOT NULL, 
                        date_dem TEXT NOT NULL,
                        done INTEGER);""")
    conn.commit()
    conn.close()

# creation de la table de la base de donner si n'estiste pas

createTable()

def insertdonnee():
    name = name_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    contact	= contact_entry.get()
    adresse	= adresse_entry.get()
    type_com = type_com_entry.get()
    nom_dom	= nom_dom_entry.get()
    activity = activity_entry.get()
    type_emp = type_emp_entry.get()
    duree = duree_entry.get()
    montant_dem	= montant_dem_entry.get()
    date_dem = date_entry.get()
    done = 0
    conn = sqlite3.connect('database/typeemp.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO information (name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant_dem,date_dem,done) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?)", (name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant_dem,date_dem,done))
    conn.commit()
    conn.close()
    effacer_champs()
    afficherdonner()

def prendredonnee():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM information WHERE done=0")
    rows = curseur.fetchall()
    conn.close()
    return rows

def prendredonneedone():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM information WHERE done='1'")
    rows = curseur.fetchall()
    conn.close()
    return rows

def metreajours():
    treevalue = treeview.selection()
    selection = treeview.selection()

    item = treeview.item(selection)
    id = int(item['values'][0])
    print(id)

    # Récupérez les valeurs des champs d'entrée
    name = name_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    adresse = adresse_entry.get()
    type_com = type_com_entry.get()
    nom_dom = nom_dom_entry.get()
    activity = activity_entry.get()
    type_emp = type_emp_entry.get()
    duree = duree_entry.get()
    montant_dem = montant_dem_entry.get()
    date_dem = date_entry.get()

    # Établissez une connexion à la base de données
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()

    # Utilisez des paramètres nommés pour plus de clarté
    curseur.execute(
        "UPDATE information SET name=?, lastname=?, email=?, contact=?, adresse=?, type_com=?, nom_dom=?, activity=?, type_emp=?, duree=?, montant_dem=?, date_dem=? WHERE id=?;",
        (name, lastname, email, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem,
         id))

    conn.commit()
    conn.close()

def afficher_details(event):
    selection = treeview.selection()
    if selection:
        item = treeview.item(selection)
        global selected_id
        selected_id = item['values'][0]
        name_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        adresse_entry.delete(0, tk.END)
        type_com_entry.delete(0, tk.END)
        nom_dom_entry.delete(0, tk.END)
        activity_entry.delete(0, tk.END)
        type_emp_entry.delete(0, tk.END)
        duree_entry.delete(0, tk.END)
        montant_dem_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        name_entry.insert(0, item['values'][1])
        lastname_entry.insert(0, item['values'][2])
        email_entry.insert(0, item['values'][3])
        contact_entry.insert(0, item['values'][4])
        adresse_entry.insert(0, item['values'][5])
        type_com_entry.insert(0, item['values'][6])
        nom_dom_entry.insert(0, item['values'][7])
        activity_entry.insert(0, item['values'][8])
        type_emp_entry.insert(0, item['values'][9])
        duree_entry.insert(0, item['values'][10])
        montant_dem_entry.insert(0, item['values'][11])
        date_entry.insert(0, item['values'][12])

def prendreemail():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT email FROM information")
    rows = curseur.fetchall()
    conn.commit()
    conn.close()
    return rows

# ------------------ Function btn -------------------------
def effacer_champs():
    name_entry.delete(0, tk.END)
    lastname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    adresse_entry.delete(0, tk.END)
    type_com_entry.delete(0, tk.END)
    nom_dom_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
    type_emp_entry.delete(0, tk.END)
    duree_entry.delete(0, tk.END)
    montant_dem_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


def afficherdonner():
    for row in treeview.get_children():
        treeview.delete(row)
    donnee = prendredonnee()
    count = 0
    for disp in donnee:
        treeview.insert(parent='', index='end', iid=count, text='', values=(disp[0],disp[1],disp[2],disp[3],disp[4],disp[5],disp[6],disp[7],disp[8],disp[9],disp[10],disp[11],disp[12]))
        count += 1
    print("afficher donner executer ")

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
info_com_titre.grid(row=0,column=3,columnspan=2) # columnspan : combiner n column

type_com_label = ttk.Label(top_frame, text="TYPE DE COMMERCE: ", width=20)
type_com_label.grid(row=1, column=3)

type_com_entry = ttk.Entry(top_frame, width=30)
type_com_entry.grid(row=1, column=4, pady=5)

nom_dom_label = ttk.Label(top_frame, text="NOM DE DOMAINE :", width=20)
nom_dom_label.grid(row=2, column=3)

nom_dom_entry = ttk.Entry(top_frame, width=30)
nom_dom_entry.grid(row=2, column=4, pady=10)

activity_label = ttk.Label(top_frame, text="ACTIVITE :", width=20)
activity_label.grid(row=3,column=3)

activity_entry = ttk.Entry(top_frame, width=30)
activity_entry.grid(row=3, column=4, pady=10)

# ------------------ RIGHT Content -------------------------
info_empr_titre = ttk.Label(top_frame,text="DETAIL DE L'EMPRUNT:", font=("Arial", 20))
info_empr_titre.grid(row=0,column=5,columnspan=2) # columnspan : combiner n column

type_emp_label = ttk.Label(top_frame, text="TYPE D'EMPRUNT :", width=20)
type_emp_label.grid(row=1, column=5, padx=10)

type_emp_entry = ttk.Combobox(top_frame,value=["Micro", "TPE", "PME", "Akanisoa", "Tranosoa 1", "Tanosoa 2", "Zarasoa"], width=27)
type_emp_entry.grid(row=1, column=6, padx=10, pady=5)

duree_label = ttk.Label(top_frame, text="DUREE :", width=20)
duree_label.grid(row=2, column=5,padx=10, )

duree_entry = ttk.Spinbox(top_frame, width=23, from_=2, to=20)
duree_entry.grid(row=2, column=6,padx=10,pady= 5)

montant_dem_label = ttk.Label(top_frame, text="MONTANT DEMANDER :", width=20)
montant_dem_label.grid(row=3, column=5)

montant_dem_entry = ttk.Entry(top_frame, width=30)
montant_dem_entry.grid(row=3, column=6,padx=10,pady= 5)

date_dem_label = ttk.Label(top_frame, text="DATE D'EMPRUNT :")
date_dem_label.grid(row=4, column=5)

date_entry = ttk.Entry(top_frame, width=30)
date_entry.grid(row=4, column=6,padx=10,pady= 5)

# ------------------ Content BTM-------------------------

update_btn = ttk.Button(top_frame, text="Envoyer email", width=20, command=lancerproc)
update_btn.grid(row=1, column=7, pady=5)

rec_btn = ttk.Button(top_frame, text="Enregistrer", width=20, command=insertdonnee) #
#, command=bdd_Bank.insertdonnee(id,name_, lastname_, email_, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem)
rec_btn.grid(row=2, column=7)

clear_btn = ttk.Button(top_frame, text="Effacer", width=20, command=effacer_champs)
clear_btn.grid(row=3, column=7, padx=10)

update_btn = ttk.Button(top_frame, text="Mettre à jours", width=20, command=metreajours)
update_btn.grid(row=4, column=7, pady=5)

actualiser_btn = ttk.Button(top_frame, text="Actualiser la table", width=20, command=afficherdonner)
actualiser_btn.grid(row=5, column=7, pady=5)

# ------------------ RIGHT FRAME -------------------------

treescroll = ttk.Scrollbar(childframe1)
treescroll.pack(side="right", fill="y")

titrepart1 = ttk.Label(btm_frame, text="En cours:", font=("Arial", 20))
titrepart1.pack()

treeview= ttk.Treeview(btm_frame, height=10) #show="headings"
# column
treeview['columns'] = ("Id","Nom","Prenom","Email","Contact","Adresse","Type de commerce","Nom du domaine","Activité","Type d'emprunt","Durée","Montant","Date d'emprunt")
treeview.column("#0", width=20, anchor="w")
treeview.column("Id", width=20, anchor="w")
treeview.column("Nom", width=150, anchor="w")
treeview.column("Prenom", width=150, anchor="w")
treeview.column("Email", width=100, anchor="w")
treeview.column("Contact", width=100, anchor="w")
treeview.column("Adresse", width=200, anchor="w")
treeview.column("Type de commerce", width=200, anchor="w")
treeview.column("Nom du domaine", width=100, anchor="w")
treeview.column("Activité", width=100, anchor="w")
treeview.column("Type d'emprunt", width=100, anchor="w")
treeview.column("Durée", width=100, anchor="w")
treeview.column("Montant", width=100, anchor="w")
treeview.column("Date d'emprunt", width=100, anchor="w")

# heading
treeview.heading("#0", text="", anchor="w")
treeview.heading("Id", text="Id", anchor="w")
treeview.heading("Nom", text="Nom", anchor="w")
treeview.heading("Prenom", text="Prenom", anchor="w")
treeview.heading("Email", text="Email", anchor="w")
treeview.heading("Contact", text="Contact", anchor="w")
treeview.heading("Adresse", text="Adresse", anchor="w")
treeview.heading("Type de commerce", text="Type de commerce", anchor="w")
treeview.heading("Nom du domaine", text="Nom du domaine", anchor="w")
treeview.heading("Activité", text="Activité", anchor="w")
treeview.heading("Type d'emprunt", text="Type d'emprunt", anchor="w")
treeview.heading("Durée", text="Durée", anchor="w")
treeview.heading("Date d'emprunt", text="Date d'emprunt", anchor="w")
treeview.heading("Montant", text="Montant", anchor="w")

treeview.bind("<ButtonRelease-1>",afficher_details)

# ---------------------------- insert data ----------------------------------

afficherdonner()

# donnee = prendredonnee()
# count = 0
# for disp in donnee:
#     treeview.insert(parent='', index='end',iid=count,text='', values=(disp[0],disp[1],disp[2],disp[3],disp[4],disp[5],disp[6],disp[7],disp[8],disp[9],disp[10],disp[11],disp[12]))
#     count += 1

treeview.pack()
treescroll.config(command=treeview.yview)
# treescroll2.config(command=treeview.xview)

# ----------------------------------------------------------------- treeview2 data ------------------------------------------------------------------------------------------

tree2label = ttk.Label(btm_frame, text="Terminer :", font=("Arial",20))
tree2label.pack()

treeview2= ttk.Treeview(btm_frame, height=10) #show="headings"
# column
treeview2['columns'] = ("Id","Nom","Prenom","Email","Contact","Adresse","Type de commerce","Nom du domaine","Activité","Type d'emprunt","Durée","Montant","Date d'emprunt")
treeview2.column("#0", width=20, anchor="w")
treeview2.column("Id", width=20, anchor="w")
treeview2.column("Nom", width=150, anchor="w")
treeview2.column("Prenom", width=150, anchor="w")
treeview2.column("Email", width=100, anchor="w")
treeview2.column("Contact", width=100, anchor="w")
treeview2.column("Adresse", width=200, anchor="w")
treeview2.column("Type de commerce", width=200, anchor="w")
treeview2.column("Nom du domaine", width=100, anchor="w")
treeview2.column("Activité", width=100, anchor="w")
treeview2.column("Type d'emprunt", width=100, anchor="w")
treeview2.column("Durée", width=100, anchor="w")
treeview2.column("Montant", width=100, anchor="w")
treeview2.column("Date d'emprunt", width=100, anchor="w")

# heading
treeview2.heading("#0", text="", anchor="w")
treeview2.heading("Id", text="Id", anchor="w")
treeview2.heading("Nom", text="Nom", anchor="w")
treeview2.heading("Prenom", text="Prenom", anchor="w")
treeview2.heading("Email", text="Email", anchor="w")
treeview2.heading("Contact", text="Contact", anchor="w")
treeview2.heading("Adresse", text="Adresse", anchor="w")
treeview2.heading("Type de commerce", text="Type de commerce", anchor="w")
treeview2.heading("Nom du domaine", text="Nom du domaine", anchor="w")
treeview2.heading("Activité", text="Activité", anchor="w")
treeview2.heading("Type d'emprunt", text="Type d'emprunt", anchor="w")
treeview2.heading("Durée", text="Durée", anchor="w")
treeview2.heading("Date d'emprunt", text="Date d'emprunt", anchor="w")
treeview2.heading("Montant", text="Montant", anchor="w")

#--------------------------------------------- insert data --------------------------------------------------
donnee2 = prendredonneedone()
count = 0
for disp in donnee2:
    treeview2.insert(parent='', index='end',iid=count,text='', values=(disp[0],disp[1],disp[2],disp[3],disp[4],disp[5],disp[6],disp[7],disp[8],disp[9],disp[10],disp[11],disp[12]))
    count += 1
treeview2.pack()


th2 = Thread(target=window.mainloop())
th2.start()
th2.join()

print("Tonga eto")

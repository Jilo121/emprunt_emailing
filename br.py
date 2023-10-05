import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Alert client")
window.geometry("1200x600")

# ------------------ frame principale -------------------------

frame = tk.Frame()
frame.pack()


style = ttk.Style(window)
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# ------------------ NAV TAB -------------------------

tabControle = ttk.Notebook(window)

add_tab = ttk.Frame(tabControle)
show_tab = ttk.Frame(tabControle)

tabControle.add(show_tab,text="Voir")
tabControle.add(add_tab,text="Nouveau")
tabControle.pack(expand=1, fill="both")


# ------------------ frame d'ajout -------------------------
add_personnal_information_frame = tk.LabelFrame(add_tab, text="Information personnelle", font=('Arial', 20))
add_personnal_information_frame.grid(row=0, column=0,pady=20)

# ------------------ formulaire d'ajout -------------------------
name_label = ttk.Label(add_personnal_information_frame, text="NOM :", width=15)
name_label.grid(row=0,column=0,padx=10)

name_entry = ttk.Entry(add_personnal_information_frame)
name_entry.grid(row=0,column=1,padx=10)

lastname_label = ttk.Label(add_personnal_information_frame, text="PRENOM :", width=15)
lastname_label.grid(row=0,column=2,padx=10, )

lastname_entry = tk.Entry(add_personnal_information_frame)
lastname_entry.grid(row=0,column=3,padx=10)

email_label = tk.Label(add_personnal_information_frame, text="EMAIL :", width=15)
email_label.grid(row=0,column=4,padx=10, )

email_entry = tk.Entry(add_personnal_information_frame)
email_entry.grid(row=0,column=5,padx=10)

contact_label = tk.Label(add_personnal_information_frame, text="CONTACTE :", width=15)
contact_label.grid(row=0,column=6,padx=10, )

contact_entry = tk.Entry(add_personnal_information_frame)
contact_entry.grid(row=0,column=7,padx=10)

# ------------------ frame d'ajout -------------------------
add_emprunt_info_frame = tk.LabelFrame(add_tab, text="Information sur l'emprunt", font=('Arial', 20))
add_emprunt_info_frame.grid(row=1, column=0)

# ------------------ formulaire d'ajout -------------------------
type_com_label = tk.Label(add_emprunt_info_frame, text="TYPE DE COMMERCE :")
type_com_label.grid(row=0,column=0,padx=10)

type_com_entry = tk.Entry(add_emprunt_info_frame)
type_com_entry.grid(row=0,column=1,padx=10)

nom_dom_label = tk.Label(add_emprunt_info_frame, text="NOM DU DOMAINE :")
nom_dom_label.grid(row=0,column=2,padx=10)

nom_dom_entry = tk.Entry(add_emprunt_info_frame)
nom_dom_entry.grid(row=0,column=3,padx=10)

activity_label = tk.Label(add_emprunt_info_frame, text="ACTIVITE :")
activity_label.grid(row=0,column=4,padx=10)

activity_entry = tk.Entry(add_emprunt_info_frame)
activity_entry.grid(row=0,column=5,padx=10)

type_empr_label = tk.Label(add_emprunt_info_frame, text="TYPE D'EMPRUNT :")
type_empr_label.grid(row=0,column=6,padx=10)

type_empr_entry = ttk.Combobox(add_emprunt_info_frame,values=["Micro","TPE","PME","Akanisoa","Tranosoa","Zarasoa"])
type_empr_entry.grid(row=0,column=7,padx=10)

montant_label = tk.Label(add_emprunt_info_frame, text="MONTANT DEMANDER :")
montant_label.grid(row=0,column=8,padx=10)

montant_entry = tk.Entry(add_emprunt_info_frame)
montant_entry.grid(row=0,column=9,padx=10)

# ------------------ frame de recherche -------------------------

search_label_frame = tk.LabelFrame(show_tab, text="Rechercher", font=('Arial', 20))
search_label_frame.grid(row=2,column=0, padx=20, pady=20)

# ------------------ formulaire de recherche -------------------------
search_label = tk.Label(search_label_frame, text="Rechercher")
search_label.grid(row=0,column=0)

donnee = ["Nosy"],["Domoina"],["Diamondra"]

search_entry_combo = ttk.Combobox(search_label_frame, values=["",donnee[0],donnee[1],donnee[2]])
search_entry_combo.grid(row=0, column=1)

window.mainloop()
import tkinter as tk
from tkinter import ttk
import bdd_Bank


def titre(frame_t,texte_t,row_t,col_t):
    titre_element = ttk.Label(chr(frame_t),chr(texte_t), width=20)
    titre_element.grid(row=int(row_t),column=int(col_t))

bdd_Bank.createTable()

def enregistrer(): #name_entry,lastname_entry, email_entry,contact_entry,adresse_entry,info_com_entry,type_com_entry,nom_dom_entry,activity_entry,type_emp_entry,duree_entry,montant_dem_entry,date_entry
    # name_ = name_entry.get()
    # lastname_ = lastname_entry.get()
    # email_ = email_entry.get()
    # contact = contact_entry.get
    # adresse = adresse_entry.get()
    # # info_com = info_com_entry.get()
    # type_com = type_com_entry.get()
    # nom_dom = nom_dom_entry.get()
    # activity = activity_entry.get()
    # type_emp = type_emp_entry.get()
    # duree = duree_entry.get()
    # montant_dem = montant_dem_entry.get()
    # date_dem = date_entry.get()

    bdd_Bank.insertdonnee()


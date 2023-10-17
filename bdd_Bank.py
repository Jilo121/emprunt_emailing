import sqlite3

def createTable():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("CREATE TABLE IF NOT EXISTS information (id_info INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, lastname TEXT NOT NULL, email TEXT NOT NULL, contact	TEXT NOT NULL, adresse	TEXT NOT NULL, type_com	TEXT NOT NULL, nom_dom	TEXT NOT NULL, activity TEXT NOT NULL, type_emp	TEXT NOT NULL, duree INTEGER NOT NULL, montant_dem	INTEGER NOT NULL, date_dem TEXT NOT NULL, PRIMARY KEY(id_info AUTOINCREMENT));")
    conn.commit()
    conn.close()

def insertdonnee():
    # Récupérer les valeurs des entrées de l'utilisateur
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

    # Insérer les données dans la base de données
    conn = sqlite3.connect('database/information.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO information(name, lastname, email, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (name_, lastname_, email_, contact, adresse, type_com, nom_dom, activity, type_emp, duree, montant_dem, date_dem))
    conn.commit()
    conn.close()

# def insertdonnee(id_info,name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem):
#     conn = sqlite3.connect('database/typeemp.db')
#     curseur = conn.cursor()
#     curseur.execute("INSERT INTO information VALUES('null,?,?,?,?,?,?,?,?,?,?,?,?,?,?')",(id_info,name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem))
#     conn.commit()
#     conn.close()

def prendredonnee():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM information")
    rows = curseur.fetchall()
    conn.commit()
    conn.close()
    return rows

def metreajours(name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("UPDATE information SET name=?, lastname=?, email=?, contact=?, adresse=?, type_com=?, nom_dom=?, activity=?, type_emp=?, duree=?, montant_dem=?, date_dem=? WHERE id_info=?;",(name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem))
    conn.commit()
    conn.close()

def metreajours(id_tab):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("UPDATE information SET terminer=1 WHERE id_info=?;",(id_tab))
    conn.commit()
    conn.close()

def deleteRec(id):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("DELETE FROM information WHERE id_info=?;", (id))
    conn.commit()
    conn.close()

def prendreemail():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT email FROM information")
    rows = curseur.fetchall()
    conn.commit()
    conn.close()
    return rows
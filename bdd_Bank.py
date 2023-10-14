import sqlite3

def createTable():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("CREATE TABLE IF NOT EXISTS information (id_info INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, lastname TEXT NOT NULL, email TEXT NOT NULL, contact	TEXT NOT NULL, adresse	TEXT NOT NULL, type_com	TEXT NOT NULL, nom_dom	TEXT NOT NULL, activity TEXT NOT NULL, type_emp	TEXT NOT NULL, duree INTEGER NOT NULL, montant_dem	INTEGER NOT NULL, date_dem TEXT NOT NULL, PRIMARY KEY(id_info AUTOINCREMENT));")
    conn.commit()
    conn.close()

def insertdonnee(id_info,name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("INSERT INTO information VALUES('null,?,?,?,?,?,?,?,?,?,?,?,?,?,?')",(id_info,name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem))
    conn.commit()
    conn.close()

def prendredonnee():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM information")
    rows = curseur.fetchall()
    conn.commit()
    conn.close()
    return rows

# test 

rowss = prendredonnee()

duree_mail = int(rowss[0][10])
send_mail = int(rowss[0][13])

print(duree_mail)
print(send_mail)

print(duree_mail - send_mail)

# def prendredonnee(done):
#     conn = sqlite3.connect('database/information.db')
#     curseur = conn.cursor()
#     curseur.execute("SELECT * FROM information WHERE done=?", done)
#     rows = curseur.fetchall()
#     conn.commit()
#     conn.close()
#     return rows

def metreajours(name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("UPDATE information SET name=?, lastname=?, email=?, contact=?, adresse=?, type_com=?, nom_dom=?, activity=?, type_emp=?, duree=?, montant_dem=?, date_dem=? WHERE id_info=?;",(name,lastname,email,contact,adresse,type_com,nom_dom,activity,type_emp,duree,montant,date_dem))
    conn.commit()
    conn.close()

def deleteRec(id):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("DELETE FROM information WHERE id_info=?;", (id))
    conn.commit()
    conn.close()
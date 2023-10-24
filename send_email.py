
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import smtplib
import sqlite3
from tkinter import messagebox


# joursrecule = timedelta(days=5)

#ajout d'email :
email = ""
app_password = ""


def prendredonnee():
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM information WHERE done=0")
    rows = curseur.fetchall()
    conn.close()
    return rows

def miseajoursnbremail(id):
    conn = sqlite3.connect('database/typeemp.db')
    curseur = conn.cursor()
    curseur.execute("UPDATE information SET done = ? WHERE id =?", (1, id))
    conn.commit()
    conn.close()

def finemail():
    datefin = date.fromisoformat(dateadhesion) - relativedelta(days=5) + relativedelta(months=int(duree))
    if (dateenvoie == datefin):
        miseajoursnbremail(id_obj)

def envoyermail(receiver,dateadhesion,duree):
    i = 0
    while i <= int(duree):
        joursenvoie = date.fromisoformat(dateadhesion) - relativedelta(days=5) + relativedelta(months=i)
        todaydate = date.today()
        if (joursenvoie == todaydate):
            print(joursenvoie)

            subject = "Rappel"
            message = "On vous fait savoir que dans 5 jours, vous devez payer une part de l'argent"
            text = f"Subject: {subject}\n\n{message}"

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, app_password)
                server.sendmail(email, receiver, text)
                print("Envoyé à", receiver)
                messagebox.showinfo(title="Email envoyer à :", message=receiver)

                if (i == int(duree)):
                    miseajoursnbremail(row[0])


            except Exception as e:
                print(e,":", receiver,"n'a pas reçus son email de rapelle")
                messagebox.showerror(title="Erreur!!",message="Erreur de connexion")

        else:
            print(" Pas d'email a envoyer ")
        i += 1


def lancerproc():
    rows = prendredonnee()

    for row in rows:
        envoyermail(row[3],row[12],row[10])
        print(row[3],row[10],row[12])
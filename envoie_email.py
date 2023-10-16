# from datetime import datetime, date, timedelta
# # import timedelta

# from dateutil.relativedelta import relativedelta

# import smtplib
# import ssl
# import schedule
# import time
# import datetime
# from dateutil.relativedelta import relativedelta

# from bdd_Bank import prendredonnee

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email import encoders

# email = "nosyhery.hasina@gmail.com"
# app_password = "yaqf jspt nnhh tsrj"

# def sending_mail(receiver):

#     subject = "Rappel"
#     message = "Alefaaaa kkkk"

#     simple_email_context = ssl.create_default_context()

#     text = f"Subject : {subject}\n\n{message}"
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()

#         server.login(email, app_password)
#         server.sendmail(email, receiver, text)
#         print("Envoyer")
#     except Exception as e:
#         print(e)

# # envoie d'email 

# rowss = prendredonnee()

# for row in rowss:
#     id_tab = int(row[0])
#     duree_mail = int(row[10])
#     send_mail = int(row[13])
#     reciever = str(row[3])
#     date_inscr = date.fromisoformat(row[11])

#     margedate = timedelta(days=5)

#     dateenvoie = date_inscr - margedate + relativedelta(months=1)

#     print("duree d'envoie de mail: ", duree_mail)
#     print("Email envoyer", send_mail)

#     print(duree_mail - send_mail)
#     print("Receiver: ", reciever)
#     print("Date: " + str(date_inscr))
#     print("Date d'envoie :", dateenvoie)

#     # Date de fin
#     date_fin = dateenvoie + relativedelta(months=duree_mail)  

#     # Planifiez l'envoi d'e-mails mensuels

#     def planifier_envoi_email():
#         while datetime.date.now() <= date_fin:
#             send_mail(reciever)
#             dateenvoie += relativedelta(months=1)
#             schedule.every().month.at(dateenvoie.strftime('08:00')).do(send_mail(reciever))
#             time.sleep(1)

#     # Démarrez le planificateur

#     planifier_envoi_email()

#     while True:
#         schedule.run_pending()
#         time.sleep(1)
    









    #chat gpt

from datetime import datetime, date, timedelta
import smtplib
import ssl
import schedule
import time
from dateutil.relativedelta import relativedelta
from bdd_Bank import prendredonnee
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "nosyhery.hasina@gmail.com"
app_password = "yaqf jspt nnhh tsrj"

def sending_mail(receiver):
    subject = "Rappel"
    message = "Alefaaaa kkkk"
    text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, app_password)
        server.sendmail(email, receiver, text)
        print("Envoyé à", receiver)
    except Exception as e:
        print(e)

# Obtenez les données de la base de données
rowss = prendredonnee()

def proc_envoie():
    for row in rowss:
        id_tab = int(row[0])
        duree_mail = int(row[10])
        send_mail = int(row[13])
        reciever = str(row[3])
        date_inscr = date.fromisoformat(row[11])

        margedate = timedelta(days=5)
        dateenvoie = date_inscr - margedate + relativedelta(months=1)

        print("Durée d'envoi de mail:", duree_mail)
        print("Email envoyé:", send_mail)
        print(duree_mail - send_mail)
        print("Destinataire:", reciever)
        print("Date d'inscription:", date_inscr)
        print("Date d'envoi:", dateenvoie)

        # Date de fin
        date_fin = dateenvoie + relativedelta(months=duree_mail)

        # Fonction pour envoyer un e-mail
        def planifier_envoi_email():
            while datetime.now().date() <= date_fin:
                sending_mail(reciever)
                dateenvoie += relativedelta(months=1)
                schedule.every().month.at(dateenvoie.strftime('08:00')).do(lambda: sending_mail(reciever))
                time.sleep(1)

        # Démarrez le planificateur
        planifier_envoi_email()

        while True:
            schedule.run_pending()
            time.sleep(1)

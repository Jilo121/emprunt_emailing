# from datetime import datetime, date, time
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

email = "nosyhery.hasina@gmail.com"
app_password = "yaqf jspt nnhh tsrj"

def sending_mail(receiver):

    subject = "Rappel"
    message = "Alefaaaa kkkk"

    simple_email_context = ssl.create_default_context()

    text = f"Subject : {subject}\n\n{message}"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(email, app_password)
        server.sendmail(email, receiver, text)
        print("Envoyer")
    except Exception as e:
        print(e)
    



sending_mail("diamondra.andriamampiandra@gmail.com")




# print(date.today())

# conversion de string en date : date.fromisoformat

# datetime.strptime => conversion en format date ::: strptime.net
# datetime.strftime => conversion date en string ::: strftime.net

# if (date.today() != date.fromisoformat("2023-10-09")):
#     print(type(date.today()))
#     print('Faux' + " 2023-10-09")
# else:
#     print('Vraie')

# print(date.today().day + 30)

# date1 = date.fromisoformat("2023-05-09")
# date2 = date.today()

# print(date1)
# print(date2)

# print(date2 - date1)
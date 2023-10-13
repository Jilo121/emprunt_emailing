from datetime import datetime, date, time
# import smtpd

print(date.today())

# conversion de string en date : date.fromisoformat

# datetime.strptime => conversion en format date ::: strptime.net
# datetime.strftime => conversion date en string ::: strftime.net

if (date.today() != date.fromisoformat("2023-10-09")):
    print(type(date.today()))
    print('Faux' + " 2023-10-09")
else:
    print('Vraie')

print(date.today().day + 30)

date1 = date.fromisoformat("2023-05-09")
date2 = date.today()

print(date1)
print(date2)

print(date2 - date1)
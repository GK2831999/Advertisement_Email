from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


import smtplib


message = MIMEMultipart()
message["from"] = "g.k.anim.tp1999@gmail.com"
message["to"] = "ftpromi0226@gmail.com"
message["subject"] = "This is a test email"
message.attach(MIMEText("Body", "plain"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("g.k.anim.tp1999@@gmail.com", "ctsnnpmijmkbdwlu")
    smtp.send_message(message)
    print("Sent...")


# ctsnnpmijmkbdwlu

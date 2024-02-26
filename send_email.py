from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
tempalte = Template(Path("Template/template.html").read_text())

# ftpromi0226@gmail.com
message = MIMEMultipart()
message["from"] = "g.k.anim.tp1999@gmail.com"
message["to"] = "golam.kibria.anim@g.bracu.ac.bd"
message["subject"] = "This is a test email"
body = tempalte.substitute(
    {"name": "Promi", "logo": "image/ZAYYANA.png"})
message.attach(MIMEText(body, "html"))


image_reader = open("Template/Image/ZAYYANA.png", 'rb')
image = MIMEImage(image_reader.read())
image_reader.close()
image.add_header('Content-ID', '<Mailtrapimage>')
message.attach(image)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("g.k.anim.tp1999@@gmail.com", "ctsnnpmijmkbdwlu")
    smtp.send_message(message)
    print("Sent...")


# ctsnnpmijmkbdwlu

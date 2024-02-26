from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template_path = "Template/template.html"
image_path = "Template/Image/ZAYYANA.png"


with open(template_path, "r") as template_file:
    template_content = template_file.read()

# Create a Template object
template = Template(template_content)


# ftpromi0226@gmail.com
message = MIMEMultipart()
message["from"] = "g.k.anim.tp1999@gmail.com"
message["to"] = "golam.kibria.anim@g.bracu.ac.bd"
message["subject"] = "This is a test email"
body = template.substitute(
    {"name": "Promi", "logo": "image/ZAYYANA.png"})
message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("image/ZAYYANA.png").read_bytes()))
with open(image_path, "rb") as image_file:
    image = MIMEImage(image_file.read())
    message.attach(image)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("g.k.anim.tp1999@@gmail.com", "ctsnnpmijmkbdwlu")
    smtp.send_message(message)
    print("Sent...")


# ctsnnpmijmkbdwlu

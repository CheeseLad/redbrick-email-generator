#!/usr/bin/env python3

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from config import sender_email, sender_password, smtp_server as smtp_server_address, smtp_port, recipients, author_info
import datetime

email_content = sys.argv[1]

with open(email_content, 'r') as file:
    html_body = file.read()

soup = BeautifulSoup(html_body, 'html.parser')

subject = soup.find('h1').text
sender = sender_email
recipients = recipients
password = sender_password

def send_email(subject, html_body, sender, recipients, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f"{author_info} <{sender}>"
    msg['To'] = ', '.join(recipients)

    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    with smtplib.SMTP_SSL(smtp_server_address, smtp_port) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f'Email: "{subject}" has been successfully sent at {current_date} to {", ".join(recipients)}')

send_email(subject, html_body, sender, recipients, password)

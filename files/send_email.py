#!/usr/bin/env python3

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from config import *
import datetime

def send_email(subject, html_body, sender, recipients, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f"{config_data['author_info']} <{sender}>"
    msg['To'] = ', '.join(recipients)

    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp_server_address:
        smtp_server_address.login(sender, password)
        smtp_server_address.sendmail(sender, recipients, msg.as_string())
        current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return f'Email: "{subject}" has been successfully sent at {current_date} to {", ".join(recipients)}'

def send_email_input(email_content):

    soup = BeautifulSoup(email_content, 'html.parser')

    subject = soup.find('h1').text
    sender = sender_email
    password = sender_password

    output = send_email(subject, email_content, sender, recipients, password)
    return output

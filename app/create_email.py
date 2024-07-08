#!/usr/bin/env python3

import os
import sys
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from event_config import *
from config import *
from send_email import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def render_template(template_path, variables):
    env = Environment(loader=FileSystemLoader(searchpath="."), keep_trailing_newline=True)
    template = env.get_template(template_path)

    output = template.render(variables)
    return output

def process(input_file):

    read_sections = {}
    structure_sections = {}

    with open(input_file, 'r') as file:
        input_content = file.read()

    soup = BeautifulSoup(input_content, 'html.parser')

    for item in config_data:
        structure_sections[item] = config_data[item]
        read_sections[item] = config_data[item]

    for tag in soup.find_all():
        tag_name_edit = tag.name.replace('-', '_')
        read_sections[tag_name_edit] = tag.text
        structure_sections[tag_name_edit] = '{{' + tag_name_edit + '}}'

    if read_sections['is_hackerclub'].lower() == 'true':
        structure_sections['hackerclub_section'] = hackerclub_section
    
    if int(read_sections['event_count']) > 0:
        structure_sections['event_section'] = event_section

        for i in range(1, int(read_sections['event_count']) + 1):
            structure_sections[f'event_{i}'] = globals()[f'event{i}']


    file_date = datetime.datetime.now().strftime("%d.%m.%Y")

    file_path = 'generated_emails/redbrick.email.' + file_date + '.html'

    output_sections = render_template('static/template.html', structure_sections)

    with open(file_path, 'w') as file:
        file.write(output_sections)

    output_final = render_template(file_path, read_sections)


    with open(file_path, 'w') as file:
        file.write(output_final)
        return file_path

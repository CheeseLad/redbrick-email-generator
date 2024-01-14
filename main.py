#!/usr/bin/env python3

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import os
import datetime
import sys
from event import *
from config import *

def render_template(template_path, variables):
    env = Environment(loader=FileSystemLoader(searchpath="."), keep_trailing_newline=True)
    template = env.get_template(template_path)

    output = template.render(variables)
    return output

def read_text_between_tags(html_content, tag_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    tag = soup.find(tag_name)

    if tag_name in ['intro-text', 'main-text', 'hackerclub-info', 'event-info']:
        return str(tag)
    else:
        return tag.get_text()

def add_events(event_count):
    event_variables = {
        'newsletter_week': '{{ newsletter_week }}',
        'events_section_title': '{{ events_section_title }}',
        'hackerclub_section_title': '{{ hackerclub_section_title }}',
        'hackerclub_link': '{{ hackerclub_link }}',
        'intro_image_url': '{{ intro_image_url }}',
        'intro_text': '{{ intro_text }}',
        'long_text': '{{ long_text }}',
        'newsletter_colour' : ' {{ newsletter_colour }}', 
        'email_colour' : '{{ email_colour }}',
        'hackerclub_title': '{{ hackerclub_title }}',
        'hackerclub_info': '{{ hackerclub_info }}',
        'hackerclub_image_url': '{{ hackerclub_image_url }}',
        'author_info': '{{ author_info }}',
        'author_year': ' {{ author_year }}',
        'facebook_img' : '{{ facebook_img }}',
        'twitter_img' : '{{ twitter_img }}',
        'instagram_img' : '{{ instagram_img }}',
        'discord_img' : '{{ discord_img }}',
    }
    if event_count == '1':
        event_variables['event_1'] = event1
    elif event_count == '2':
        event_variables['event_1'] = event1
        event_variables['event_2'] = event2
    else:
        print("Invalid event count.")
        exit()
    before_template_path = 'template.html'
    rendered_content2 = render_template(before_template_path, event_variables)

    with open('template-event.html', 'w') as output_file:
      output_file.write(rendered_content2)


def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()

    tokens = []
    sections = ['week', 'event-count', 'events-section-title', 'hackerclub-section-title', 'event-link', 'intro-gif', 'intro-text', 'main-text', 'hackerclub-title', 'hackerclub-info', 'hackerclub-image', 'event-title', 'event-info', 'event-image']
    for section in sections:
        temp = (read_text_between_tags(html_content, section).lstrip().rstrip())
        temp = temp.replace('\n', '<br>')
        tokens.append(temp)
    
    add_events(tokens[1])
    
    template_variables = {
        'newsletter_week': tokens[0],
        'event_count': tokens[1],
        'events_section_title': tokens[2],
        'hackerclub_section_title': tokens[3],
        'hackerclub_link': tokens[4],
        'event_1_link': tokens[4],
        'intro_image_url': tokens[5],
        'intro_text': tokens[6],
        'long_text': tokens[7],

        'hackerclub_title': tokens[8],
        'hackerclub_info': tokens[9],
        'hackerclub_image_url': tokens[10],

        'event_1_title': tokens[11],
        'event_1_info': tokens[12],
        'event_1_image_url': tokens[13],

        'event_2_title': tokens[11],
        'event_2_info': tokens[12],
        'event_2_image_url': tokens[13],

        'newsletter_colour' : newsletter_colour, 
        'email_colour' : email_colour, 
        'author_info': author_info,
        'author_year': author_year,
        'facebook_img' : facebook_img,
        'twitter_img' : twitter_img,
        'instagram_img' : instagram_img,
        'discord_img' : discord_img
    }
    template_path = 'template-event.html'
    rendered_content = render_template(template_path, template_variables)

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    if "emails" not in os.listdir():
       os.mkdir("emails")

    file_path = './emails/redbrick.email.' + current_date + '.html'
       
    with open(file_path, 'w') as output_file:
      output_file.write(rendered_content)

if __name__ == "__main__":
    try:
      main(sys.argv[1])
    except IndexError:
        print("Please provide a file path to the newsletter markdown file.")
        exit()

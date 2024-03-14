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

    if tag_name in ['intro-text', 'main-text']:
        return str(tag)
    else:
        return tag.get_text()

def add_events(event_count):
    event_variables = {
        'email_title': '{{ email_title }}',
        'intro_image_url': '{{ intro_image_url }}',
        'intro_text': '{{ intro_text }}',
        'long_text': '{{ long_text }}',
        'newsletter_colour' : ' {{ newsletter_colour }}', 
        'email_colour' : '{{ email_colour }}',
        'author_info': '{{ author_info }}',
        'author_year': ' {{ author_year }}',
        'facebook_img' : '{{ facebook_img }}',
        'twitter_img' : '{{ twitter_img }}',
        'instagram_img' : '{{ instagram_img }}',
        'discord_img' : '{{ discord_img }}',
    }
    before_template_path = 'template-update.html'
    rendered_content2 = render_template(before_template_path, event_variables)

    with open('template-update.html', 'w') as output_file:
      output_file.write(rendered_content2)


def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()

    tokens = []
    sections = ['email-title', 'intro-gif', 'intro-text', 'main-text',]
    for section in sections:
        temp = (read_text_between_tags(html_content, section).lstrip().rstrip())
        temp = temp.replace('\n', '<br>')
        tokens.append(temp)
    
    add_events(tokens[1])
    
    template_variables = {
        'email_title': tokens[0],
        'intro_image_url': tokens[1],
        'intro_text': tokens[2],
        'long_text': tokens[3],


        'newsletter_colour' : newsletter_colour, 
        'email_colour' : email_colour, 
        'author_info': author_info,
        'author_year': author_year,
        'facebook_img' : facebook_img,
        'twitter_img' : twitter_img,
        'instagram_img' : instagram_img,
        'discord_img' : discord_img
    }

    
    template_path = 'template-update.html'
    rendered_content = render_template(template_path, template_variables)

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    if "emails" not in os.listdir():
       os.mkdir("emails")

    file_path = './emails/redbrick.single-email.' + current_date + '.html'
       
    with open(file_path, 'w') as output_file:
      output_file.write(rendered_content)

if __name__ == "__main__":
    #try:
      main(sys.argv[1])
    #except IndexError:
    #    print("Please provide a file path to the newsletter markdown file.")
    #    exit()

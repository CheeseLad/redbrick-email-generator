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

    tag_list = ['intro-text', 'main-text', 'hackerclub-info']

    """if event_count == '1':
        tag_list.append('event1-info')
    
    if event_count == '2':
        tag_list.append('event1-info')
        tag_list.append('event2-info')"""

    if tag_name in tag_list:
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
        event_variables['event_section'] = event_section
        event_variables['event_1'] = event1


    if event_count == '2':
        event_variables['event_section'] = event_section
        event_variables['event_1'] = event1
        event_variables['event_2'] = event2

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

    event_count_html = read_text_between_tags(html_content, 'event-count')
    is_hackerclub_html = read_text_between_tags(html_content, 'is-hackerclub')

    tokens = []
    sections = ['week', 'event-count', 'events-section-title', 'hackerclub-section-title', 'event-link', 'intro-gif', 'is-hackerclub', 'intro-text', 'main-text']
    if is_hackerclub_html.lower() == 'true':
        sections.append('hackerclub-title')
        sections.append('hackerclub-info')
        sections.append('hackerclub-image')
    if event_count_html == '1':
        sections.append('event1-title')
        sections.append('event1-info')
        sections.append('event1-image')
    if event_count_html == '2':
        sections.append('event1-title')
        sections.append('event1-info')
        sections.append('event1-image')
        sections.append('event2-title')
        sections.append('event2-info')
        sections.append('event2-image')
    
    if event_count_html == '3':
        sections.append('event1-title')
        sections.append('event1-info')
        sections.append('event1-image')
        sections.append('event2-title')
        sections.append('event2-info')
        sections.append('event2-image')
        sections.append('event3-title')
        sections.append('event3-info')
        sections.append('event3-image')

    if event_count_html == '4':
        sections.append('event1-title')
        sections.append('event1-info')
        sections.append('event1-image')
        sections.append('event2-title')
        sections.append('event2-info')
        sections.append('event2-image')
        sections.append('event3-title')
        sections.append('event3-info')
        sections.append('event3-image')
        sections.append('event4-title')
        sections.append('event4-info')
        sections.append('event4-image')

    if event_count_html == '5':
        sections.append('event1-title')
        sections.append('event1-info')
        sections.append('event1-image')
        sections.append('event2-title')
        sections.append('event2-info')
        sections.append('event2-image')
        sections.append('event3-title')
        sections.append('event3-info')
        sections.append('event3-image')
        sections.append('event4-title')
        sections.append('event4-info')
        sections.append('event4-image')
        sections.append('event5-title')
        sections.append('event5-info')
        sections.append('event5-image')
        
    for section in sections:
        temp = (read_text_between_tags(html_content, section).lstrip().rstrip())
        temp = temp.replace('\n', '<br>')
        tokens.append(temp)
    
    add_events(tokens[1])
    
    template_variables = {
        'newsletter_week': tokens[0],
        'event_count': tokens[1],
        'hackerclub_section_title': tokens[3],
        'hackerclub_link': tokens[4],
        'event_link': tokens[4],
        'intro_image_url': tokens[5],
        'intro_text': tokens[7],
        'long_text': tokens[8],

        'newsletter_colour' : newsletter_colour, 
        'email_colour' : email_colour, 
        'author_info': author_info,
        'author_year': author_year,
        'facebook_img' : facebook_img,
        'twitter_img' : twitter_img,
        'instagram_img' : instagram_img,
        'discord_img' : discord_img
    }

    if tokens[6].lower() == 'true':
        template_variables['hackerclub_title'] = tokens[9]
        template_variables['hackerclub_info'] = tokens[10]
        template_variables['hackerclub_image_url'] = tokens[11]


    if tokens[1] == '1':
      template_variables['events_section_title'] = tokens[2]
      template_variables['event_1_title'] = tokens[12]
      template_variables['event_1_info'] = tokens[13]
      template_variables['event_1_image_url'] = tokens[14]

    if tokens[1] == '2':
      template_variables['events_section_title'] = tokens[2]
      template_variables['event_1_title'] = tokens[12]
      template_variables['event_1_info'] = tokens[13]
      template_variables['event_1_image_url'] = tokens[14]
      template_variables['event_2_title'] = tokens[15]
      template_variables['event_2_info'] = tokens[16]
      template_variables['event_2_image_url'] = tokens[17]

    if tokens[1] == '3':
        template_variables['events_section_title'] = tokens[2]
        template_variables['event_1_title'] = tokens[12]
        template_variables['event_1_info'] = tokens[13]
        template_variables['event_1_image_url'] = tokens[14]
        template_variables['event_2_title'] = tokens[15]
        template_variables['event_2_info'] = tokens[16]
        template_variables['event_2_image_url'] = tokens[17]
        template_variables['event_3_title'] = tokens[18]
        template_variables['event_3_info'] = tokens[19]
        template_variables['event_3_image_url'] = tokens[20]

    if tokens[1] == '4':
        template_variables['events_section_title'] = tokens[2]
        template_variables['event_1_title'] = tokens[12]
        template_variables['event_1_info'] = tokens[13]
        template_variables['event_1_image_url'] = tokens[14]
        template_variables['event_2_title'] = tokens[15]
        template_variables['event_2_info'] = tokens[16]
        template_variables['event_2_image_url'] = tokens[17]
        template_variables['event_3_title'] = tokens[18]
        template_variables['event_3_info'] = tokens[19]
        template_variables['event_3_image_url'] = tokens[20]
        template_variables['event_4_title'] = tokens[21]
        template_variables['event_4_info'] = tokens[22]
        template_variables['event_4_image_url'] = tokens[23]

    if tokens[1] == '5':
        template_variables['events_section_title'] = tokens[2]
        template_variables['event_1_title'] = tokens[12]
        template_variables['event_1_info'] = tokens[13]
        template_variables['event_1_image_url'] = tokens[14]
        template_variables['event_2_title'] = tokens[15]
        template_variables['event_2_info'] = tokens[16]
        template_variables['event_2_image_url'] = tokens[17]
        template_variables['event_3_title'] = tokens[18]
        template_variables['event_3_info'] = tokens[19]
        template_variables['event_3_image_url'] = tokens[20]
        template_variables['event_4_title'] = tokens[21]
        template_variables['event_4_info'] = tokens[22]
        template_variables['event_4_image_url'] = tokens[23]
        template_variables['event_5_title'] = tokens[24]
        template_variables['event_5_info'] = tokens[25]
        template_variables['event_5_image_url'] = tokens[26]
    
    template_path = 'template-event.html'
    rendered_content = render_template(template_path, template_variables)

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    if "emails" not in os.listdir():
       os.mkdir("emails")

    file_path = './emails/redbrick.email.' + current_date + '.html'
       
    with open(file_path, 'w') as output_file:
      output_file.write(rendered_content)

if __name__ == "__main__":
    main(sys.argv[1])

#!/usr/bin/env python3

# This file contains all the configuration variables for the newsletter

# Newsletter configuration

config_data = {
  'newsletter_colour': '#ffffff', # Colour of the newsletter buttons
  'email_colour': '#ffffff', # Colour of the email footer text
  'author_info': 'John Doe', # Name
  'author_year': 'Secretary 2023-2024', # Year and Position
  'facebook_img': 'https://url.com/facebook.png', # Replace with your own images
  'twitter_img': 'https://url.com/twitter.png', # Replace with your own images
  'instagram_img': 'https://url.com/instagram.png', # Replace with your own images
  'discord_img': 'https://url.com/discord.png' # Replace with your own images
}

# Email configuration

sender_email = 'example@example.com' # Email address
sender_password = 'password' # Email password
smtp_server = 'smtp.example.com' # SMTP server
smtp_port = 465 # SMTP port
recipients = ['example1@example.com', 'example2@example.com'] # Recipient email addresses
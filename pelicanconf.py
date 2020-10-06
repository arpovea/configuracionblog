#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Adrián Rodríguez Povea'
SITENAME = 'Blog Informático'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'


#Carpeta donde se genera la web
OUTPUT_PATH = '../blog-web/'

#Carpeta del tema elegido
THEME = './blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#Paginación:
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#Configuración del Tema:

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU (True)

# Display categories list on the top menu
#DISPLAY_CATEGORIES_ON_MENU (True)

# Display categories list as a submenu of the top menu
#DISPLAY_CATEGORIES_ON_SUBMENU (False)

# Display the category in the article's info
#DISPLAY_CATEGORIES_ON_POSTINFO (False)

# Display the author in the article's info
#DISPLAY_AUTHOR_ON_POSTINFO (False)

# Display the search form
#DISPLAY_SEARCH_FORM (False)

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE (Title)

# Display the "Fork me on Github" banner
#GITHUB_URL (None)

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
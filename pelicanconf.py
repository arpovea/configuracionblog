#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Adrián Rodríguez Povea'
SITENAME = "Blog Informático"
SITEURL = 'https://arpovea.vercel.app'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

#Carpeta donde se genera la web
OUTPUT_PATH = '../blog-web/'

#Paginación:
DEFAULT_PAGINATION = 10

# Theme
THEME = './MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'

# Author
AUTHOR_INTRO = u'¡Hola Mundo! Mi nombre es Adrián.'
AUTHOR_DESCRIPTION = u'Apasionado de las tecnologías.'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://arpovea.vercel.app'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'arpovea'

# Social
SOCIAL = (
    ('facebook', 'http://www.facebook.com/johndoe'),
    ('twitter', 'http://twitter.com/johndoe'),
    ('github', 'https://github.com/johndoe'),
    ('linkedin', 'http://www.linkedin.com/in/johndoe'),
)

# Menu
MENUITEMS = (
    ('Categorías', '/categories.html'),
    ('Articulos', '/archives.html'),
)
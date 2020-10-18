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
DEFAULT_PAGINATION = 5

# Theme
THEME = './MinimalXY'

#Opciones Markdown:

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'theme/images/arpovealogo.PNG'

# Author
AUTHOR_INTRO = u'¡Hola Mundo! Mi nombre es Adrián.'
AUTHOR_DESCRIPTION = u'Apasionado de las tecnologías.'
AUTHOR_AVATAR = 'theme/images/arpovealogo.PNG'
AUTHOR_WEB = 'http://arpovea.vercel.app'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'arpovea'

# Social
SOCIAL = (
#    ('facebook', 'http://www.facebook.com/'),
    ('twitter', 'http://twitter.com/arodriguezpovea'),
    ('github', 'https://github.com/arpovea'),
    ('linkedin', 'http://www.linkedin.com/in/arpovea'),
)

# Menu
MENUITEMS = (
    ('Categorías', '/categories.html'),
    ('Artículos', '/archives.html'),
)
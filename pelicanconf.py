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
AUTHOR_INTRO = u'Hello world! I’m John Doe.'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://mypersonalsite.com'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'johndoe'

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
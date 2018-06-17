#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Serge Bouchut'
SITENAME = u'resume'
SITEURL = 'https://sergebouchut.github.io/resume'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'resume'

NAME = 'Serge Bouchut'
TAGLINE = 'Software Engineer'
PIC = 'profile.png'

EMAIL = 'serge.bouchut@gmail.com'
PHONE = '(+33) 6 31 65 95 68'
WEBSITE = 'https://sergebouchut.github.io/blog/'
LINKEDIN = 'sergebouchut'
GITHUB = 'SergeBouchut'

CAREER_SUMMARY = ''

SKILLS = [
    {'title': 'Python', 'level': 80},
    {'title': 'JavaScript', 'level': 60},
    {'title': 'PHP', 'level': 40},
    {'title': 'C#', 'level': 40},
    {'title': 'Java', 'level': 40},
]

PROJECT_INTRO = ''

PROJECTS = [
    {'title': '', 'tagline': ''},
]

LANGUAGES = [
    {'name': 'French', 'description': 'Native'},
    {'name': 'English', 'description': 'Professional'},
]

INTERESTS = ['Machine learning', 'Piano', 'Salsa', 'Running']

EXPERIENCES = [
    {
        'job_title': 'Software engineer',
        'time': '',
        'company': 'Forcity, Lyon',
        'details': '',
    },
    {
        'job_title': 'Software engineer',
        'time': '',
        'company': 'Multiposting (SAP SuccessFactors), Paris',
        'details': '',
    },
    {
        'job_title': 'Software engineer / project manager',
        'time': '',
        'company': 'Harmonie Technologie, Paris',
        'details': '',
    },
]

EDUCATIONS = [
    {
        'degree': '',
        'meta': '',
        'time': '',
    }
]

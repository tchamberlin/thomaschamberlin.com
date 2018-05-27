#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Chamberlin'
SITENAME = 'Thomas Chamberlin'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (('GitHub', 'http://github.com/tchamberlin'),)

DEFAULT_PAGINATION = None
THEME = f"../pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'series']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# SIDEBAR = "sidebar.html"
# CUSTOM_SIDEBAR_MIDDLES = ("sb_taglist.html", )

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
# SITELOGO = SITEURL + '/images/profile.jpg'

AVATAR = 'images/profile.jpg'
# AVATAR = None
ABOUT_ME = "I like to build stuff"
BANNER = 'images/banner.jpg'

# SHOW_ARTICLE_CATEGORY = True


# Series
# SHOW_SERIES = True
# DISPLAY_SERIES_ON_SIDEBAR = True

# CC Footer
CC_LICENSE = "CC-BY"

# GitHub sidebar info
GITHUB_USER = 'tchamberlin'
GITHUB_REPO_COUNT = True
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Include breadcrumbs at top
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Chamberlin'
SITENAME = 'Thomas Chamberlin'
SITEURL = ''

# Path to site content
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
SOCIAL = (('GitHub', 'http://github.com/tchamberlin'),)

DEFAULT_PAGINATION = 10
THEME = "../pelican-themes/pelican-bootstrap3"

# NOTE: This might need to change if this repo is forked!
PLUGIN_PATHS = ['../pelican-plugins']
# i18n_subsites is required for pelican-bootstrap3, even if you aren't using translations
PLUGINS = ['i18n_subsites', 'series', 'tipue_search', 'tag_cloud', 'pin_to_top']
# Again, required for pelican-bootstrap3
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# SHOW_DATE_MODIFIED = True

# DISPLAY_ARTICLE_INFO_ON_INDEX = True

AVATAR = 'images/profile.jpg'
ABOUT_ME = "I like to build stuff"
BANNER = 'images/banner.jpg'

# This is only here to include search
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Series
SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = True

# Enable tag display in sidebar
DISPLAY_TAGS_ON_SIDEBAR = True
# This enables the tag cloud
DISPLAY_TAGS_INLINE = True

# CC Footer
CC_LICENSE = "CC-BY"

# GitHub sidebar info
# GITHUB_USER = 'tchamberlin'
# GITHUB_REPO_COUNT = 5
# GITHUB_SKIP_FORK = 'true'
# GITHUB_SHOW_USER_LINK = 'true'

# Include breadcrumbs at top
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

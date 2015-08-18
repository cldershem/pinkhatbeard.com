#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.errors
~~~~~~~~~~~~~~~~~

Default errors for the entire application unless overridden.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/pinkhatbeard.com
"""
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html',
                           adj1='human',
                           adj2='talented',
                           adj3='might make mistakes')


@main.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500`.html',
                           adj1='human',
                           adj2='talented',
                           adj3='might make mistakes')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.controller.py
~~~~~~~~~~~~~~~~~

Main routes for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/pinkhatbeard.com
"""
from flask import render_template
from . import main
import random
from collections import namedtuple


def get_contacts():
    Contact = namedtuple('Contact', 'label, display, link')
    list_of_contacts = [
        Contact('email', 'cameron [at] pinkhatbeard.com', None),
        Contact('phone', '+1.312.361.0322', 'tel:+013123610322'),
        Contact('github', 'github.com/cldershem',
                'http://github.com/cldershem'),
        Contact('gitlab', 'gitlab.com/cldershem',
                'http://gitlab.com/cldershem'),
        Contact('gitlab phb', 'gitlab.com/pinkhatbeard',
                'http://gitlab.com/pinkhatbeard'),
        Contact('twitter', '@jerknextdoor',
                'https://twitter.com/jerknextdoor'),
        Contact('resume', 'github.com/cldershem/resume',
                'https://github.com/cldershem/Resume/' +
                'blob/master/built/CameronDershemResume-Skills.pdf'),
        Contact('freenode', 'jerknextdoor', None),
        Contact('keybase.io', 'cldershem', 'https://keybase.io/cldershem'),
        Contact('skype', 'cldershem', 'callto://cldershem'),
        Contact('linkedin', 'Cameron Dershem',
                'https://www.linkedin.com/in/cameron-dershem-1462389'),
        Contact('google+', '+CameronDershem',
                'http://google.com/+CameronDershem'),
        Contact('last.fm', 'cldershem', 'http://last.fm/user/cldershem'),
        Contact('ttn', 'cldershem',
                'https://www.thethingsnetwork.org/u/cldershem/'),
        ]

    return list_of_contacts


@main.route('/')
@main.route('/index')
def index():
    list_o_adjs = [
        "loud",
        "glasses",
        "talks a lot",
        "likes bikes",
        "long-haired",
        "hair farmer",
        "carries a purse",
        ]

    adj1 = 'pink hat'
    adj2 = 'beard'
    adj3 = random.choice(list_o_adjs)

    return render_template('index.html',
                           adj1=adj1,
                           adj2=adj2,
                           adj3=adj3,
                           contacts=get_contacts())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.controller.py
~~~~~~~~~~~~~~~~~

Main routes for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
from flask import render_template
from . import main
import random


@main.route('/')
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
                           adj3=adj3)

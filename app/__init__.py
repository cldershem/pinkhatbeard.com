#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
app.py
~~~~~~~~~~~~~~~~~

This is an application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REP
"""
from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_module
    from .api import api as api_module

    app.register_blueprint(main_module)
    app.register_blueprint(api_module)

    return app

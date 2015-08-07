#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
manage.py
~~~~~~~~~~~~~~~~~

Baremetal/maintenance for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/pinkhatbeard.com
"""
from app import create_app
from flask.ext.script import Manager


app = create_app('development')
manager = Manager(app)


@manager.command
@manager.option('--environment', 'e', help='development, production, test')
def run(environment='development'):
    """
    """
    app = create_app(environment)
    app.run()


@manager.command
@manager.option('--environment', 'e', help='development, production, test')
def run_on_network(environment='development'):
    """
    """
    app = create_app('development')
    app.run('0.0.0.0')


@manager.command
def show_config():
    """
    Pretty prints current config.
    """
    from pprint import pprint

    print("Config:")
    pprint(dict(app.config))


@manager.command
def populate_db():
    """
    Populates db from yaml source.
    """
    # from app.models import *
    from app import db
    import os

    dev_db = './tmp/dev.sqlite'

    if os.path.isfile(dev_db):
        os.rename(dev_db, dev_db + '.bak')

    db.create_all()


if __name__ == '__main__':
    manager.run()

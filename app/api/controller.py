#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
api.controller.py
~~~~~~~~~~~~~~~~~

Controller for the api

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/pinkhatbeard.com
"""
from flask import jsonify
from . import api


class Response():
    """
    """
    def __init__(self, success=False, data=None, error=None,
                 page=None, **kwargs):
        self.success = success
        if error:
            self.error = error
        if data:
            self.data = data
        if page:
            self.page = page

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_json(self):
        return jsonify(self.__dict__)

    def __repr__(self):
        return "<Response success={}, data={}, error={}>".format(
            self.success, self.data, self.error)


@api.route('/')
def api_index():
    # raise api.APIError('API docs, not yet implemented.', status_code=501)
    return Response(message='API not yet implemented.').to_json(), 501

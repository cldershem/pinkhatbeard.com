#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
app.models
~~~~~~~~~~~~~~~~~

DB models for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
from app import db, bcrypt
import datetime
from .utils import (serializer, timed_serializer)
from itsdangerous import (BadSignature, SignatureExpired)
from flask import render_template
from .emails import send_email


class User(db.Model):
    """
    Defines db model for `User`.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(50))
    _password = db.Column(db.String(50))
    confirmed = db.Column(db.DateTime())
    _last_seen = db.Column(db.DateTime())
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    _is_active = db.Column(db.Boolean())
    _api_key = db.Column(db.String(50))
    # roles

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password)
        return password

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self):
        self._api_key = bcrypt.generate_password_hash(self.email)
        return self._api_key

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        """
        Returns `True` if user is logged in.  Returns `False` if user
        not logged in.
        """
        return False

    def activate(self):
        self.confirmed = datetime.datetime.utcnow()
        # self.roles.can_login = True
        self._is_active = True

    def is_active(self):
        if not self.confirmed or not self._is_active:
            return False
        return True

    def get_id(self):
        return str(self.email)

    def __repr__(self):
        return '<User {}, {}>'.format(self.firstname, self.email)

    def __unicode__(self):
        return self.email

    def is_admin(self):
        pass

    @property
    def last_seen(self):
        return self._last_seen

    @last_seen.setter
    def last_seen(self, date):
        self._last_seen = date
        return self.last_seen

    @staticmethod
    def get(email=None, **kwargs):
        """
        if no **kwargs, returns list of all active.
        """
        if email:
            try:
                return User.query.filter_by(email=email).first()
            except:
                return False
        if kwargs:
            return [user for user in
                    User.query.filter_by(is_active=True,
                                         **kwargs).all()]
        else:
            return [user for user in
                    User.query.filter_by(is_active=True).all()]

    @staticmethod
    def get_activation_link(user):
        user_id = user.get_id()
        s = serializer()
        payload = s.dumps(user_id)
        return payload

    @staticmethod
    def check_activation_link(payload):
        s = serializer()
        try:
            user_id = s.loads(payload)
        except BadSignature:
            return False
        return user_id

    @staticmethod
    def get_password_reset_link(user):
        #     return False
        user_id = user.get_id()
        s = timed_serializer()

        # disallows password reset link to be reused
        old_hash = user.password[:10]
        payload = s.dumps(user_id + old_hash)
        return payload

    @staticmethod
    def check_password_reset_link(payload):
        s = timed_serializer()

        try:
            # disallows password reset link to be reused
            unhashed_payload = s.loads(payload, max_age=86400)
            old_hash = unhashed_payload[
                len(unhashed_payload)-10:len(unhashed_payload)]
            user_id = unhashed_payload[:-10]
            user = User.get(email=user_id)
        except SignatureExpired or BadSignature:
            return False
        return (user, old_hash)

    @staticmethod
    def create(new_user):
        db.session.add(new_user)
        db.session.commit()
        payload = User.get_activation_link(new_user)
        User.email_confirmation(new_user, payload)

        # TODO: make this work
        new_user.save()

        new_user = User.get(email=new_user.email)
        return new_user

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.get(email=self.email)

    @staticmethod
    def email_confirmation(user, payload):
        """
        """
        subject = "[adamOwes] - confirm email"
        recipients = [user.email]
        text_body = render_template("emails/email_confirmation.txt",
                                    user=user, payload=payload)
        html_body = render_template("emails/email_confirmation.html",
                                    user=user, payload=payload)

        send_email(subject, recipients, text_body, html_body)
        return True

    @staticmethod
    def email_password_reset(user, payload):
        """
        """
        subject = "[adamOwes] - password reset"
        recipients = [user.email]
        text_body = render_template("emails/password_reset.txt",
                                    user=user, payload=payload)
        html_body = render_template("emails/password_reset.html",
                                    user=user, payload=payload)

        send_email(subject, recipients, text_body, html_body)

        return True

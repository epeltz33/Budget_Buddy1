from .db import db
from flask_login import UserMixin as LoginMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, LoginMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now(), server_onupdate=db.func.now())

    @property  # This is a decorator so that we can call it like a function
    def password(self):
            return self.hashed_password

    @password.setter  # This is a setter method for the password property
    def password(self, password):
            self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
            return check_password_hash(self.hashed_password, password)

    def to_dict(self):
            return {
                'id': self.id,
                'username': self.username,
                     'email': self.email,
                     'created_at': self.created_at,
                     'updated_at': self.updated_at

            }

#!/usr/bin/env python3

"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password using bcrypt.

        :param password: The password to hash.
        :return: The hashed password as bytes.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        :param email: The email of the user.
        :param password: The password of the user.
        :return: The newly created User object.
        :raises ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

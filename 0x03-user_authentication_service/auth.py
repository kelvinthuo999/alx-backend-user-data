#!/usr/bin/env python3

"""
Auth module
"""
import bcrypt

def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    :param password: The password to hash.
    :return: The hashed password as bytes.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

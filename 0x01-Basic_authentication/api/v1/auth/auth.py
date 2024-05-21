#!/usr/bin/env python3

from typing import List
from flask import request

class Auth:
    """Class for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required."""
        return False

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header."""
        return None

    def current_user(self, request=None):
        """Method to get the current user."""
        return None

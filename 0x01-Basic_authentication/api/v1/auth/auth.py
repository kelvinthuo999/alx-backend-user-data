#!/usr/bin/env python3

from typing import List
from flask import request

class Auth:
    """Class for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required."""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header."""
        return None

    def current_user(self, request=None):
        """Method to get the current user."""
        return None

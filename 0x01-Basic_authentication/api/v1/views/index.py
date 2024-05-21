#!/usr/bin/env python3
"""Index views module."""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Raises a 401 Unauthorized error"""
    abort(401)


@app_views.route('/forbidden')
def trigger_forbidden_error():
    """
    Raise a 403 error
    """
    abort(403)

#!/usr/bin/env python3

"""
Basic Flask app with user registration endpoint
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"])
def welcome():
    """
    GET route that returns a JSON payload.
    """
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users():
    """
    POST /users route to register a user.
    Expects form data fields: "email" and "password".
    """
    email = request.form.get('email')
    password = request.form.get('password')
    
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

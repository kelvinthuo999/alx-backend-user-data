#!/usr/bin/env python3
"""API entry point."""
#!/usr/bin/env python3
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(401)
def unauthorized(error):
    """Handler for 401 errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """
    Handler for 403
    """
    return jsonify({'error': 'Forbidden'}), 403


if __name__ == "__main__":
    import os
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)

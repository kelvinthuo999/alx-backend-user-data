# api/v1/views/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Import all view modules to register routes
from api.v1.views.index import *

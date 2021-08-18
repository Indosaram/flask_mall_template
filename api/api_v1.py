"""Item API"""

from flask import Blueprint

from .item import api as item_api

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(item_api)

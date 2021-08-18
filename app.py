"""Main app"""

from flask import (
    Flask,
    render_template,
    Blueprint,
)

from model.item import db
from api.api_v1 import api


def create_app(config_path="flask_config.py"):
    """Flask app factory function"""
    app = Flask(__name__)
    app.config.from_pyfile(config_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    home = Blueprint('home', __name__)

    @home.route("/")
    def index():
        return render_template("index.html")

    app.register_blueprint(home)
    app.register_blueprint(api)

    return app


def init_db():
    """initialize db by command line
    $ python3 -c "from app import init_db; init_db()"
    """
    db.create_all(app=create_app())
